from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IncomeViewSet

router = DefaultRouter()
router.register("", IncomeViewSet, basename="income")

urlpatterns = [
    path("", include(router.urls)),
]