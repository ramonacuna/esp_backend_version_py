from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import  TipoContratoViewSet,TipoEmpresasViewSet,EmpresasViewSet

router = DefaultRouter()
router.register(r'tipos-contratos', TipoContratoViewSet)
router.register(r'tipo-empresas', TipoEmpresasViewSet)

urlpatterns = [
    path('',include(router.urls)),
]