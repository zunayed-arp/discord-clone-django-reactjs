from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import AllowOriginAPIViewSerializer, IpListSerializer, UserSerializer, AllowOriginSerializer
from project.models import AllowOrigin, IpList
from django.contrib.auth import get_user_model

#user
User = get_user_model()


class AllowOriginViewSet(viewsets.ModelViewSet):
    serializer_class = AllowOriginSerializer
    queryset = AllowOrigin.objects.all()

    def create(self, request, *args, **kwargs):
        print(request)
        return super().create(request, *args, **kwargs)


class IpListViewSet(viewsets.ModelViewSet):
    serializer_class = IpListSerializer
    queryset = IpList.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class AllowOriginAPIView(APIView):
    serializer_class = AllowOriginAPIViewSerializer

    def get_object(self, pk):
        try:
            return AllowOrigin.objects.get(pk=pk)
        except AllowOrigin.DoesNotExist:
            raise Http404

    #    def get(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet)
    #     return Response(serializer.data)

    def get(self, request, id=None, *args, **kwargs):
        if id:
            allow_origin = self.get_object(id)
            serializer = AllowOriginAPIViewSerializer(allow_origin)
            return Response(serializer.data)
        else:
            obj = AllowOrigin.objects.all()
            serializer = self.serializer_class(obj, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, id=None, format=None):
        allow_origin = self.get_object(id)
        serializer = AllowOriginAPIViewSerializer(
            allow_origin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def patch(self, request, id=None):
        allow_origin = self.get_object(id)
        serializer = AllowOriginAPIViewSerializer(allow_origin, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id=None, format=None):
        snippet = self.get_object(id)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
