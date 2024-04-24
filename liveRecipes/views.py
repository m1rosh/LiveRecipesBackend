from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def process_data(request):
    if request.method == 'POST':
        # Получаем данные из запроса
        data = request.body  # Для данных формы
        # data = request.body  # Для данных в формате JSON

        # Обработка данных
        # Например, вы можете сохранить данные в модели или выполнить другие операции
        print(data)
        # Возвращаем ответ
        return JsonResponse({'message': 'Data processed '})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})


class MainPageRecipeList(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = serializers.MainPageRecipeSerializer


class OneRecipeInfo(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
    lookup_field = 'id'


class RecipeList(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer


class DessertsList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='dessert')[0].recipes.all()
        serializer_class = serializers.RecipeSerializer
    except:
        pass


class GarnishList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='garnish')[0].recipes.all()
        serializer_class = serializers.RecipeSerializer
    except:
        pass


class DrinksList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='drink')[0].recipes.all()
        serializer_class = serializers.RecipeSerializer
    except:
        pass


class FirstDishList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='firstDish')[0].recipes.all()
        serializer_class = serializers.RecipeSerializer
    except:
        pass


class SecondDishList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='secondDish')[0].recipes.all()
        serializer_class = serializers.RecipeSerializer
    except:
        pass


class SaladsList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='salad')[0].recipes.all()
        serializer_class = serializers.RecipeSerializer
    except:
        pass


class SauceList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='sauce')[0].recipes.all()
        serializer_class = serializers.RecipeSerializer
    except:
        pass


class BakeryList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='bakery')[0].recipes.all()
        serializer_class = serializers.RecipeSerializer
    except:
        pass


class HarvestingList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='harvesting')[0].recipes.all()
        serializer_class = serializers.RecipeSerializer
    except:
        pass


class SnackList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='snack')[0].recipes.all()
        serializer_class = serializers.RecipeSerializer
    except:
        pass
