from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from reports.services import get_financial_summary

from expenses.models import Expense
from savings.models import SavingsGoal
from budgets.models import Budget

from django.db.models import Sum


class DashboardView(APIView):

    permission_classes = [
        IsAuthenticated
    ]


    def get(self, request):

        user = request.user


        # Financial summary

        summary = get_financial_summary(
            user=user
        )


        # Dashboard cards

        cards = {

            "income": summary["total_income"],

            "expenses": summary["total_expenses"],

            "savings": summary["total_saved"],

            "balance": summary["balance"]

        }

        # Financial health score

        if summary["financial_health"] == "Excellent":

            health_score = 90

            health_message = (
                "Your finances are in excellent condition"
            )


        elif summary["financial_health"] == "Good":

            health_score = 70

            health_message = (
                "Your finances are stable"
            )


        else:

            health_score = 40

            health_message = (
                "Consider reducing expenses and increasing savings"
            )


        financial_health = {

            "score": health_score,

            "status": summary["financial_health"],

            "message": health_message

        }


        # Expense chart data

        expense_breakdown = (
            Expense.objects
            .filter(user=user)
            .values("category")
            .annotate(
                total=Sum("amount")
            )
        )


        chart_labels = []

        chart_values = []


        for item in expense_breakdown:

            chart_labels.append(
                item["category"]
            )

            chart_values.append(
                item["total"]
            )


        # Budget alerts

        budget_alerts = []


        budgets = Budget.objects.filter(
            user=user
        )


        for budget in budgets:

            spent = Expense.objects.filter(

                user=user,

                category=budget.category

            ).aggregate(

                total=Sum("amount")

            )["total"] or 0



            if spent > budget.monthly_limit:

                status = "Exceeded"

                message = (
                    "You have exceeded your budget"
                )


            elif spent >= budget.monthly_limit * 0.8:

                status = "Warning"

                message = (
                    "You have used 80% of your budget"
                )


            else:

                status = "Safe"

                message = (
                    "Your spending is within budget"
                )



            budget_alerts.append({

                "category": budget.get_category_display(),

                "budget_limit": budget.monthly_limit,

                "spent": spent,

                "status": status,

                "message": message

            })


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


        # Final dashboard response

        return Response({

            "message": "Dashboard data retrieved successfully",

            "user": request.user.username,


            "cards": cards,


            "financial_summary": summary,

            "financial_health": financial_health,


            "expense_chart": {

                "labels": chart_labels,

                "values": chart_values

            },


            "budget_alerts": budget_alerts,


            "recent_expenses": expense_data,


            "savings_goals": savings_data

        })