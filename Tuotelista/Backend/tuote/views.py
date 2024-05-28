from tuote.permissions import IsOwnerOrReadOnly
from .models import TuoteModel
from .serializers import UserSerializer
from .serializers import TuoteSerializer
from rest_framework import permissions, generics, viewsets

from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import logout

class TuoteList(generics.ListCreateAPIView):
    queryset = TuoteModel.objects.all()
    serializer_class = TuoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class TuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TuoteModel.objects.all()
    serializer_class = TuoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class TuoteImage(generics.RetrieveAPIView):
    queryset = TuoteModel.objects.all()
    serializer_class = TuoteSerializer

class TuoteViewSet(viewsets.ModelViewSet):
    queryset = TuoteModel.objects.all()
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
                   
            for output in TuoteModel.objects.all()]
        return Response(output)
        
    def post(self, request):
        serializer = TuoteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LogoutView(APIView):
    """
    Djano 5 does not have GET logout route anymore, so Django Rest Framework UI can't log out.
    This is a workaround until Django Rest Framework implements POST logout.
    Details: https://github.com/encode/django-rest-framework/issues/9206
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        logout(request)
        return redirect('/')