from rest_framework import serializers

from .models import SavingsGoal


class SavingsGoalSerializer(serializers.ModelSerializer):

    progress = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()


    class Meta:
        model = SavingsGoal

        fields = [
            "id",
            "user",
            "name",
            "target_amount",
            "current_amount",
            "deadline",
            "description",
            "progress",
            "status",
            "created_at",
            "updated_at",
        ]

        read_only_fields = (
            "id",
            "user",
            "progress",
            "created_at",
            "updated_at",
        )


    def get_progress(self, obj):

        if obj.target_amount == 0:
            return 0

        progress = (
            obj.current_amount /
            obj.target_amount
        ) * 100

        return round(min(progress, 100), 2)

    def get_status(self, obj):

        if obj.target_amount == 0:
            return "No Target"

        progress = (
            obj.current_amount /
            obj.target_amount
        ) * 100


        if progress >= 100:
            return "Completed"

        elif progress >= 75:
            return "Almost There"

        elif progress >= 25:
            return "In Progress"

        else:
            return "Starting"