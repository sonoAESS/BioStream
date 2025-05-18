from django.shortcuts import render
from rest_framework import viewsets
from .models import Secuencia
from .serializers import SecuenciaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class SecuenciaViewSet(viewsets.ModelViewSet):
    queryset = Secuencia.objects.all()
    serializer_class = SecuenciaSerializer

    @action(detail=True, methods=['get'])
    def reverso_complementario(self, request, pk=None):
        secuencia_obj = self.get_object()
        rev_comp = reverso_complementario(secuencia_obj.secuencia)
        return Response({'reverso_complementario': rev_comp}, status=status.HTTP_200_OK)