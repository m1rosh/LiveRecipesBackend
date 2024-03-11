from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from .models import *


class RecipeList(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer


class DessertsList(generics.ListAPIView):
    queryset = Tag.objects.filter(dish_type='dessert')[0].recipes.all()
    serializer_class = serializers.RecipeSerializer


class GarnishList(generics.ListAPIView):
    queryset = Tag.objects.filter(dish_type='garnish')[0].recipes.all()
    serializer_class = serializers.RecipeSerializer


class DrinksList(generics.ListAPIView):
    queryset = Tag.objects.filter(dish_type='drink')[0].recipes.all()
    serializer_class = serializers.RecipeSerializer


class FirstDishList(generics.ListAPIView):
    queryset = Tag.objects.filter(dish_type='firstDish')[0].recipes.all()
    serializer_class = serializers.RecipeSerializer


class SecondDishList(generics.ListAPIView):
    queryset = Tag.objects.filter(dish_type='secondDish')[0].recipes.all()
    serializer_class = serializers.RecipeSerializer


class SaladsList(generics.ListAPIView):
    queryset = Tag.objects.filter(dish_type='salad')[0].recipes.all()
    serializer_class = serializers.RecipeSerializer


class SauceList(generics.ListAPIView):
    queryset = Tag.objects.filter(dish_type='sauce')[0].recipes.all()
    serializer_class = serializers.RecipeSerializer


class BakeryList(generics.ListAPIView):
    queryset = Tag.objects.filter(dish_type='bakery')[0].recipes.all()
    serializer_class = serializers.RecipeSerializer


class HarvestingList(generics.ListAPIView):
    queryset = Tag.objects.filter(dish_type='harvesting')[0].recipes.all()
    serializer_class = serializers.RecipeSerializer


class SnackList(generics.ListAPIView):
    queryset = Tag.objects.filter(dish_type='snack')[0].recipes.all()
    serializer_class = serializers.RecipeSerializer


