from django.shortcuts import render
from rest_framework import viewsets
from .models import TipoEmpresas
from .serializers import TipoEmpresasSerializer
from rest_framework.permissions import AllowAny

# Create your views here.

class TipoEmpresasViewSet(viewsets.ModelViewSet):
    queryset = TipoEmpresas.objects.all()
    serializer_class = TipoEmpresasSerializer
    permission_classes = [AllowAny]