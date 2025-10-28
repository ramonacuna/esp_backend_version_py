from django.shortcuts import render
from rest_framework import viewsets
from .models import TipoContratos
from .serializers import TipoContratosSerializer
from rest_framework.permissions import AllowAny


# Create your views here.

class TipoContratoViewSet(viewsets.ModelViewSet):
    queryset = TipoContratos.objects.all()
    serializer_class = TipoContratosSerializer
    permission_classes = [AllowAny]






