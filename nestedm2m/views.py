from django.shortcuts import render
from .models import IpList,AllowOrigin
from .serializers import IpListSerializer,AllowOriginSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class AllowOriginAPIView(APIView):
    def get(self,request,id=None):
        object = AllowOrigin.objects.all()
        serializer = AllowOriginSerializer(object,many=True)
        return Response(serializer.data)
        
