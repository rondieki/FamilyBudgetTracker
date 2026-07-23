from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Sum


from expenses.models import Expense

from .models import Budget
from .serializers import BudgetSerializer



class BudgetViewSet(viewsets.ModelViewSet):

    serializer_class = BudgetSerializer

    permission_classes = [
        IsAuthenticated
    ]


    def get_queryset(self):

        return Budget.objects.filter(
            user=self.request.user
        )


    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user
        )

    @action(
    detail=False,
    methods=["get"]
)
    def alerts(self, request):

        user = request.user

        budgets = Budget.objects.filter(
            user=user
        )

        alerts = []


        for budget in budgets:

            spent = Expense.objects.filter(
                user=user,
                category=budget.category
            ).aggregate(
                total=Sum("amount")
            )["total"] or 0


            percentage = (
                spent /
                budget.monthly_limit
            ) * 100


            if percentage > 100:

                status = "Exceeded"

                message = (
                    f"You exceeded your "
                    f"{budget.category} budget by "
                    f"{spent - budget.monthly_limit}"
                )


            elif percentage >= 80:

                status = "Warning"

                message = (
                    f"You are close to your "
                    f"{budget.category} budget limit"
                )


            else:

                status = "Safe"

                message = (
                    f"Your {budget.category} spending "
                    f"is within budget"
                )


            alerts.append({

                "category": budget.category,

                "budget_limit": budget.monthly_limit,

                "spent": spent,

                "status": status,

                "message": message

            })


        return Response(alerts)