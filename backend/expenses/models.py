from django.conf import settings
from django.db import models


class Expense(models.Model):

    class ExpenseCategory(models.TextChoices):
        HOUSING = "HOUSING", "Housing"
        FOOD = "FOOD", "Food"
        TRANSPORT = "TRANSPORT", "Transport"
        UTILITIES = "UTILITIES", "Utilities"
        HEALTHCARE = "HEALTHCARE", "Healthcare"
        EDUCATION = "EDUCATION", "Education"
        ENTERTAINMENT = "ENTERTAINMENT", "Entertainment"
        SHOPPING = "SHOPPING", "Shopping"
        SAVINGS = "SAVINGS", "Savings"
        OTHER = "OTHER", "Other"

    class PaymentMethod(models.TextChoices):
        CASH = "CASH", "Cash"
        MPESA = "MPESA", "M-Pesa"
        BANK = "BANK", "Bank Transfer"
        CARD = "CARD", "Debit/Credit Card"
        OTHER = "OTHER", "Other"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="expenses"
    )

    category = models.CharField(
        max_length=20,
        choices=ExpenseCategory.choices
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    date = models.DateField()

    payment_method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-date", "-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.amount}"