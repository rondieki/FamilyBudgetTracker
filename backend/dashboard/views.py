from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from income.models import Income
from expenses.models import Expense


class DashboardSummaryView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        total_income = (
            Income.objects.filter(
                user=request.user
            ).aggregate(
                total=Sum("amount")
            )["total"] or 0
        )

        total_expenses = (
            Expense.objects.filter(
                user=request.user
            ).aggregate(
                total=Sum("amount")
            )["total"] or 0
        )

        balance = total_income - total_expenses

        data = {
            "total_income": total_income,
            "total_expenses": total_expenses,
            "balance": balance,
            "income_records": Income.objects.filter(
                user=request.user
            ).count(),
            "expense_records": Expense.objects.filter(
                user=request.user
            ).count(),
        }

        return Response(data)