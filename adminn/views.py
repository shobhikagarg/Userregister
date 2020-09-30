# noinspection PyUnresolvedReferences
from django.shortcuts import render
# noinspection PyUnresolvedReferences
from rest_framework import status, generics
# noinspection PyUnresolvedReferences
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
# noinspection PyUnresolvedReferences
from rest_framework.decorators import api_view, permission_classes
# noinspection PyUnresolvedReferences
from rest_framework.views import APIView
# noinspection PyUnresolvedReferences
from rest_framework import viewsets
# noinspection PyUnresolvedReferences
#from .permissions import IsOwner
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import RegistrationSerializer,UserLoginSerializer,ProfileSerializer
# noinspection PyUnresolvedReferences
from .models import Account,Userr
# noinspection PyUnresolvedReferences
from rest_framework.authtoken.models import Token

class AccountViewset(viewsets.ViewSet):
    def list(self,request):
        queryset=Account.objects.all()
        serializer=RegistrationSerializer(queryset,many=True)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"Fail": "failed"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Success": "login successful"}, status=status.HTTP_201_CREATED)
# Create your views here.
class UserLoginAPIView(APIView):
    def get(self, request, format=None):
        accounts=Account.objects.all()
        serializer = UserLoginSerializer(accounts,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({"Success": "login successful"}, status=status.HTTP_200_OK)
        return Response({"message":"failed"}, status=status.HTTP_400_BAD_REQUEST)

class ProfileAPI(viewsets.ViewSet):
    def list(self, request):
        queryset = Account.objects.all()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Profilegenericview(generics.GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Account.objects.all()
    serializer_class=ProfileSerializer
    lookup_field = 'id'

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id):
        return self.destroy(request,id)
