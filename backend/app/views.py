from django.shortcuts import render
from .models import User, Fath, Kid
from .serializers import LoginSer, RegisterSer, FathSer, KidSer
from rest_framework import viewsets, views
from rest_framework.decorators import action
from rest_framework.authentication import authenticate
from rest_framework import permissions, status
from rest_framework.response import Response
from .token import Token
from django.http import Http404
from .permissions import CoolPerm
from rest_framework.authtoken.models import Token
# Create your views here.


class AuthVS(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @action(methods=['post'], detail=False)
    def register(self, request):
        serializer = RegisterSer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'data': 
                         {'username':user.username,
                          'message':'Register successfully'}}, status=status.HTTP_201_CREATED)


    @action(methods=['post'], detail=False)
    def login(self, request):
        serializer = LoginSer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if not user:
            return Response({'data': {
                'message': 'You invalid crendintails'
            }}, status=status.HTTP_400_BAD_REQUEST)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'data':{
            'username': user.username,
            'token': token.key,
            'created': created,
            'message': 'Login successfully'
        }}, status=status.HTTP_200_OK)
    

class FathMVS(viewsets.ModelViewSet):
    queryset=Fath.objects.all()
    serializer_class=FathSer
    permission_classes=[permissions.IsAuthenticated, CoolPerm]


class KidMVS(viewsets.ModelViewSet):
    queryset=Kid.objects.all()
    serializer_class=KidSer
    permission_classes=[permissions.IsAuthenticated, CoolPerm]
        

