from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import  TipoEmpresasViewSet

router = DefaultRouter()
router.register(r'tipo-empresas', TipoEmpresasViewSet)

urlpatterns = [
    path('',include(router.urls)),
]