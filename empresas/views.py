from django.shortcuts import render
from rest_framework import viewsets
from .models import Empresas
from .serializers import EmpresasSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer
    permission_classes = [AllowAny]
