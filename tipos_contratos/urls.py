from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import  TipoContratoViewSet

router = DefaultRouter()
router.register(r'tipos-contratos', TipoContratoViewSet)

urlpatterns = [
    path('',include(router.urls)),
]