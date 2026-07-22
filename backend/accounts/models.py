from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    CURRENCY_CHOICES = [
        ("KES", "Kenyan Shilling"),
        ("USD", "US Dollar"),
        ("EUR", "Euro"),
        ("GBP", "British Pound"),
    ]

    phone_number = models.CharField(max_length=20, blank=True)

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True
    )

    preferred_currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES,
        default="KES",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username