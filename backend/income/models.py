from django.conf import settings
from django.db import models


class Income(models.Model):

    class IncomeSource(models.TextChoices):
        SALARY = "SALARY", "Salary"
        BUSINESS = "BUSINESS", "Business"
        FREELANCE = "FREELANCE", "Freelance"
        INVESTMENT = "INVESTMENT", "Investment"
        GIFT = "GIFT", "Gift"
        OTHER = "OTHER", "Other"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="incomes"
    )

    source = models.CharField(
        max_length=20,
        choices=IncomeSource.choices
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    date_received = models.DateField()

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
        ordering = ["-date_received", "-created_at"]

    def __str__(self):
        return f"{self.user.username} - {self.source} - {self.amount}"