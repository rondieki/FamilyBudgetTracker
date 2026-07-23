from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .services import get_financial_summary


class FinancialSummaryView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        summary = get_financial_summary(
            request.user
        )

        return Response(summary)