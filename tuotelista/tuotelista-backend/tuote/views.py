import json
from django import forms
from django.http import HttpRequest, HttpResponse, JsonResponse
from .forms import LoginForm
from tuote.permissions import IsAdminUserOrReadOnly
from .models import TuoteModel
from .serializers import TuoteSerializer#, LoginSerializer, UserSerializer
from rest_framework import permissions, generics, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import *

from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import logout, authenticate, login



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        #'users': reverse('user-list', request=request, format=format),
        'tuote': reverse('tuote-list', request=request, format=format)
    })

class TuoteList(generics.ListCreateAPIView):
    queryset = TuoteModel.objects.all()
    serializer_class = TuoteSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUserOrReadOnly]

    #def perform_create(self, serializer):
        #serializer.save(owner=self.request.user)

class TuoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TuoteModel.objects.all()
    serializer_class = TuoteSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdminUserOrReadOnly]

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
        

"""
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


#class LoginView(APIView):
#    def get(self, request):
#        user = User.objects.all()
#        serializer = UserSerializer(user, context={'request': request})
#        return Response(serializer.data)
#    
#    def post(self, request):
#        user = authenticate(username=request.data['username'], password=request.data['password'])
#        if user:
#            token, created = Token.objects.get_or_create(user=user)
#            return Response({'token': token.key})
#        else:
#            return Response({'error': 'Invalid credentials'}, status=401)



class ReactLoginView(APIView):

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, context={'request': request}, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        #Check if user exists, return token if it does.
        data = json.load(request)
        print(data)
        form = LoginForm(data)
        serializer_obj = LoginSerializer(data=form, many=data)
        print(serializer_obj)
        print(serializer_obj.is_valid())
        if serializer_obj.is_valid():
            user = authenticate(nimi=serializer_obj.data['nimi'], salasana=serializer_obj.data['salasana'])
            print(user)
            if not user:
                return Response({'error': 'Invalid Credentials'}, status=404)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=200)
        print(serializer_obj.errors)

        return Response( status=400)
        

    #def post(self, request):
    #    Check if user exists, return token if it does.
    #    nimi = request.POST.get('nimi', '')
    #    salasana = request.POST.get('salasana', '')
    #
    #    user = authenticate(nimi=nimi, salasana=salasana)
    #    if not user:
    #        return Response({'error': 'Invalid Credentials'}, status=404)
    #    token, _ = Token.objects.get_or_create(user=user)
    #    return Response({'token': token.key}, status=200)


class LogoutView(APIView):

    #Django 5 does not have GET logout route anymore, so Django Rest Framework UI can't log out.
    #This is a workaround until Django Rest Framework implements POST logout.
    #Details: https://github.com/encode/django-rest-framework/issues/9206

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        logout(request)
        return redirect("/")
"""
