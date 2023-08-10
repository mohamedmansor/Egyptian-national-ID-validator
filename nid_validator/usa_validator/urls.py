from django.urls import path, include
from .views import USANIDValidationViewSet

urlpatterns = [
    path('', USANIDValidationViewSet.as_view({'post': 'create'})),
]