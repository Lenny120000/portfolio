from .models import Tuote
from .serializers import TuoteSerializer
from rest_framework import generics, viewsets

from rest_framework.views import APIView
from django.shortcuts import render
from . models import *
from rest_framework.response import Response

class TuoteList(generics.ListCreateAPIView):
    queryset = Tuote.objects.all()
    serializer_class = TuoteSerializer

class TuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tuote.objects.all()
    serializer_class = TuoteSerializer

class TuoteImage(generics.RetrieveAPIView):
    queryset = Tuote.objects.all()
    serializer_class = TuoteSerializer

class TuoteViewSet(viewsets.ModelViewSet):
    queryset = Tuote.objects.all()
    serializer_class = TuoteSerializer

class ReactView(APIView):
    def get(self, request):
        output = [{
            "id": output.id,
            "nimi": output.nimi,
            "hinta": output.hinta,
            "kuvaus": output.kuvaus,
            "tuotekuva": f'http://localhost:8000{output.tuotekuva.url}',
            }
                   
            for output in Tuote.objects.all()]
        return Response(output)
        
    def post(self, request):
        serializer = TuoteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)