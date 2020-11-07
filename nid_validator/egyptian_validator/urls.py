from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import NIDValidationViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r'validate', NIDValidationViewSet, basename='validate')


urlpatterns = [
    path('', include(router.urls)),
]
