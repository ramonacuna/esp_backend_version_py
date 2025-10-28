from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import  EmpresasViewSet

router = DefaultRouter()
router.register(r'empresas', EmpresasViewSet)

urlpatterns = [
    path('',include(router.urls)),
]