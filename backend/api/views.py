from django.shortcuts import render
from rest_framework import viewsets
from .models import Secuencia
from .serializers import SecuenciaSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .utils import *

class SecuenciaViewSet(viewsets.ModelViewSet):
    queryset = Secuencia.objects.all()
    serializer_class = SecuenciaSerializer

    @action(detail=True, methods=['get'])
    def reverso_complementario(self, request, pk=None):
        try:
            secuencia_obj = self.get_object()
            rev_comp = reverso_complementario(secuencia_obj.secuencia)
            return Response({'reverso_complementario': rev_comp}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=True, methods=['get'])
    def traducir_seq(self, request, pk=None):
        try:
            secuencia_obj = self.get_object()
            traduction = traducir_secuencia_adn(secuencia_obj.secuencia)
            return Response ({'traduction':traduction}, status=status.HTTP_200_OK)
        except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
    @action(detail=False, methods=['post'])
    def alinear(self, request):
        seq1 = request.data.get('seq1')
        seq2 = request.data.get('seq2')
        if not seq1 or not seq2:
            return Response({'error': 'Se requieren dos secuencias'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            resultado = alinear_secuencias(seq1, seq2)
            return Response({'alineamiento': resultado}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)