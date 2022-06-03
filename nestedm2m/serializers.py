from dataclasses import fields
from unicodedata import name
from venv import create
from wsgiref.validate import validator
from .models import IpList, AllowOrigin, Recipe, Ingredient
from rest_framework import serializers


class IpListSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpList
        fields = '__all__'


class AllowOriginSerializer(serializers.ModelSerializer):
    ip_list = IpListSerializer()

    class Meta:
        model = AllowOrigin
        fields = '__all__'


class AllowOriginCreateSerializer(serializers.ModelSerializer):
    ip_list = IpListSerializer(many=True)

    class Meta:
        model = AllowOrigin
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeMainSerializer(serializers.ModelSerializer):
    # ingredients = IngredientSerializer(many=True)
    ingredients = serializers.StringRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeCreateSerializer(RecipeMainSerializer):
    ingredients = serializers.ListField(write_only=True)

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient in ingredients_data:
            ingredient, created = Ingredient.objects.get_or_create(
                name=ingredient)
            recipe.ingredients.add(ingredient)
        return recipe


# class RecipeUpdateSerializer(serializers.ModelSerializer):
#     from rest_framework.fields import empty

#     def __init__(self, instance=None, data=empty, **kwargs):
#         self.original_data = data
#         super().__init__(instance, data, **kwargs)

#     def update(self, instance, validated_data):
#         items_dict = self.original_data

#         if 'ip_list' in items_dict:
#             ids = [item['id'] for item in items_dict['ip_list']]
#             instance_data = instance.ip_list
#             instance_data.set(ids)

#         instance = super().update(instance=instance, validated_data=validated_data)
#         instance.save()
#         return instance

#     class Meta:
#         model = Recipe
#         fields = '__all__'
# class RecipeUpdateSerializer(serializers.ModelSerializer):

#     ingredients = IngredientSerializer(many=True, read_only=False)

#     class Meta:
#         model = Recipe
#         fields = '__all__'

#     def update(self, instance, validated_data):
#         ingredients_data = validated_data.pop('ingredients')
#         instance = super(RecipeUpdateSerializer, self).update(
#             instance, validated_data)
#         for ingredient_data in ingredients_data:
#             ingredient_qs = Ingredient.objects.filter(
#                 name__iexact=ingredient_data['name'])
#             if ingredient_qs.exists():
#                 ingredients= ingredient_qs.first()
#             else:
#                 ingredients = Ingredient.objects.create(**ingredient_data)

#             instance.ingredients.add(ingredients)
#         return instance
class RecipeUpdateSerializer(serializers.ModelSerializer):

    ingredients = IngredientSerializer(many=True, read_only=False)

    class Meta:
        model = Recipe
        fields = '__all__'

    
    
    def to_internal_value(self, data):
        recipie_id = data.get('id')
        
        return super().to_internal_value(data)
