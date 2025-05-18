from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SecuenciaViewSet

router = DefaultRouter()
router.register(r"secuencias", SecuenciaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
