from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db.models import Sum

from income.models import Income
from expenses.models import Expense
from savings.models import SavingsGoal



class FinancialSummaryView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        user = request.user


        total_income = Income.objects.filter(
            user=user
        ).aggregate(
            total=Sum("amount")
        )["total"] or 0


        total_expenses = Expense.objects.filter(
            user=user
        ).aggregate(
            total=Sum("amount")
        )["total"] or 0


        total_saved = SavingsGoal.objects.filter(
            user=user
        ).aggregate(
            total=Sum("current_amount")
        )["total"] or 0


        # Expense breakdown by category
        expense_breakdown = Expense.objects.filter(
            user=user
        ).values(
            "category"
        ).annotate(
            total=Sum("amount")
        )


        # Convert queryset into dictionary
        expense_data = {}

        for item in expense_breakdown:

            category_display = dict(
                Expense.ExpenseCategory.choices
            ).get(
                item["category"],
                item["category"]
            )

            expense_data[category_display] = item["total"]


        balance = (
            total_income
            -
            total_expenses
            -
            total_saved
        )


        if total_income > 0:

            saving_rate = (
                total_saved /
                total_income
            ) * 100

        else:

            saving_rate = 0

        expense_ratio = 0

        if total_income > 0:

            expense_ratio = (
                total_expenses /
                total_income
            ) * 100

        if saving_rate >= 20:

            financial_health = "Excellent"


        elif saving_rate >= 10:

            financial_health = "Good"


        elif saving_rate > 0:

            financial_health = "Needs Improvement"


        else:

            financial_health = "Poor"


        return Response({

            "total_income": total_income,

            "total_expenses": total_expenses,

            "total_saved": total_saved,

            "balance": balance,

            "saving_rate": round(
                saving_rate,
                2
            ),

            "expense_ratio": round(
                expense_ratio,
                2
            ),

            "financial_health": financial_health,

            "expense_breakdown": expense_data
            

        })