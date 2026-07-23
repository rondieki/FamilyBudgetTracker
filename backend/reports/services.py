from django.db.models import Sum

from income.models import Income
from expenses.models import Expense
from savings.models import SavingsGoal



def get_financial_summary(user):

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



    balance = (
        total_income -
        total_expenses
    )


    if total_income > 0:

        saving_rate = (
            total_saved /
            total_income
        ) * 100

    else:

        saving_rate = 0



    if total_income > 0:

        expense_ratio = (
            total_expenses /
            total_income
        ) * 100

    else:

        expense_ratio = 0



    if expense_ratio < 50:

        financial_health = "Excellent"

    elif expense_ratio < 80:

        financial_health = "Good"

    else:

        financial_health = "Needs Improvement"



    return {

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

        "financial_health": financial_health

    }