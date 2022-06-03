from django.shortcuts import render
from .models import IpList, AllowOrigin, Recipe, Ingredient
from .serializers import IpListSerializer, AllowOriginSerializer, IngredientSerializer, RecipeMainSerializer, RecipeCreateSerializer,RecipeUpdateSerializer
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.response import Response


class RecipieView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeMainSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return RecipeCreateSerializer
        if self.action =='update':
            return RecipeUpdateSerializer
        return RecipeMainSerializer

class AllowOriginAPIView(APIView):
    def get(self, request, id=None):
        object = AllowOrigin.objects.all()
        ips = IpList.objects.all()
        serializer = AllowOriginSerializer(object, many=True)
        return Response({
            "allow": serializer.data,
            "ips": IpListSerializer(ips, many=True).data
        })

    def post(self, request, id=None):
        # data = request.data
        serializer = AllowOriginSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
        return Response(serializer.data)
