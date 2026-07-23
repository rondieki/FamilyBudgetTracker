from django.http import request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from reports.services import get_financial_summary

from expenses.models import Expense
from savings.models import SavingsGoal
from budgets.models import Budget


class DashboardView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def get(self, request):

        user = request.user

        summary = get_financial_summary(
            user=user
        )


        # Recent expenses

        recent_expenses = Expense.objects.filter(
            user=user
        ).order_by(
            "-date"
        )[:5]


        expense_data = []

        for expense in recent_expenses:

            expense_data.append({

                "category": expense.get_category_display(),

                "amount": expense.amount,

                "date": expense.date,

                "description": expense.description

            })


        # Savings goals

        savings_goals = SavingsGoal.objects.filter(
            user=user
        )


        savings_data = []

        for goal in savings_goals:

            progress = 0

            if goal.target_amount > 0:

                progress = (
                    goal.current_amount /
                    goal.target_amount
                ) * 100


            savings_data.append({

                "name": goal.name,

                "target": goal.target_amount,

                "saved": goal.current_amount,

                "progress": round(progress, 2)

            })


        return Response({

            "message": "Dashboard data retrieved successfully",

            "user": request.user.username,

            "financial_summary": summary,

            "recent_expenses": expense_data,

            "savings_goals": savings_data

        })