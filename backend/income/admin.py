from django.contrib import admin

from .models import Income


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "source",
        "amount",
        "date_received",
    )

    list_filter = (
        "source",
        "date_received",
    )

    search_fields = (
        "user__username",
        "description",
    )