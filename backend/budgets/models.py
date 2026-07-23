from django.db import models
from django.conf import settings

from expenses.models import Expense


class Budget(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


    category = models.CharField(
        max_length=50,
        choices=Expense.ExpenseCategory.choices
    )


    monthly_limit = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    updated_at = models.DateTimeField(
        auto_now=True
    )


    def __str__(self):

        return f"{self.category} Budget"