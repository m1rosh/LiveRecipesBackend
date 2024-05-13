from django.db.models.functions import Length
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from . import serializers
from django.contrib.auth.models import User
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse


@csrf_exempt
def process_data(request):
    if request.method == 'POST':
        data = request.body
        print(data)
        return JsonResponse({'message': 'Data processed '})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})


def backend_info(request):
    return render(request, 'info.html')


class CustomPagination(PageNumberPagination):
    page_size = 15

    def get_paginated_response(self, data):
        return Response(data)


@api_view(['GET'])
def recipes_feed(request):
    queryset = Recipe.objects.order_by('?')
    paginator = CustomPagination()
    result_page = paginator.paginate_queryset(queryset, request)
    serializer = serializers.MainPageRecipeSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def search(request, query):
    queryset = Recipe.objects.all()
    if query:
        queryset = queryset.filter(name__iregex=query)
    serializer = serializers.MainPageRecipeSerializer(queryset, many=True)
    return Response(serializer.data)


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
        serializer_class = serializers.MainPageRecipeSerializer
    except:
        pass


class GarnishList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='garnish')[0].recipes.all()
        serializer_class = serializers.MainPageRecipeSerializer
    except:
        pass


class DrinksList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='drink')[0].recipes.all()
        serializer_class = serializers.MainPageRecipeSerializer
    except:
        pass


class FirstDishList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='firstDish')[0].recipes.all()
        serializer_class = serializers.MainPageRecipeSerializer
    except:
        pass


class SecondDishList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='secondDish')[0].recipes.all()
        serializer_class = serializers.MainPageRecipeSerializer
    except:
        pass


class SaladsList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='salad')[0].recipes.all()
        serializer_class = serializers.MainPageRecipeSerializer
    except:
        pass


class SauceList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='sauce')[0].recipes.all()
        serializer_class = serializers.MainPageRecipeSerializer
    except:
        pass


class BakeryList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='bakery')[0].recipes.all()
        serializer_class = serializers.MainPageRecipeSerializer
    except:
        pass


class HarvestingList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='harvesting')[0].recipes.all()
        serializer_class = serializers.MainPageRecipeSerializer
    except:
        pass


class SnackList(generics.ListAPIView):
    try:
        queryset = Tag.objects.filter(dish_type='snack')[0].recipes.all()
        serializer_class = serializers.MainPageRecipeSerializer
    except:
        pass

@api_view(['GET'])
def searchBreakfast(request, query):
    queryset = Tag.objects.filter(dish_type='salad')[0].recipes.all()
    if query:
        queryset = queryset.filter(name__iregex=query)
    serializer = serializers.MainPageRecipeSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def searchLunch(request, query):
    queryset = Tag.objects.filter(dish_type='firstDish')[0].recipes.all()
    if query:
        queryset = queryset.filter(name__iregex=query)
    serializer = serializers.MainPageRecipeSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def searchDinner(request, query):
    queryset = Tag.objects.filter(dish_type='secondDish')[0].recipes.all()
    if query:
        queryset = queryset.filter(name__iregex=query)
    serializer = serializers.MainPageRecipeSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def searchSnack(request, query):
    queryset = Tag.objects.filter(dish_type='snack')[0].recipes.all()
    if query:
        queryset = queryset.filter(name__iregex=query)
    serializer = serializers.MainPageRecipeSerializer(queryset, many=True)
    return Response(serializer.data)

# class Filters(generics.ListAPIView):
#     queryset = Recipe.objects.all()
#     serializer_class = serializers.RecipeSerializer

@api_view(['GET'])
def filtersSearch(request):
    queryset = Recipe.objects.all()

    query = request.GET.get('query', None)
    caloriesl = request.GET.get('caloriesl', None)
    proteinl = request.GET.get('proteinl', None)
    fatsl = request.GET.get('fatsl', None)
    carbohydratesl = request.GET.get('carbohydratesl', None)
    caloriesm = request.GET.get('caloriesm', None)
    proteinm = request.GET.get('proteinm', None)
    fatsm = request.GET.get('fatsm', None)
    carbohydratesm = request.GET.get('carbohydratesm', None)
    duration = request.GET.get('duration', None)
    ingredient2y = request.GET.get('ingredient2y', None)
    ingredient2n = request.GET.get('ingredient2n', None)
    keyword2 = request.GET.get('keyword2', None)
    ingredient3y = request.GET.get('ingredient3y', None)
    ingredient3n = request.GET.get('ingredient3n', None)
    keyword3 = request.GET.get('keyword3', None)
    ingredient4y = request.GET.get('ingredient4y', None)
    ingredient4n = request.GET.get('ingredient4n', None)
    keyword4 = request.GET.get('keyword4', None)
    ingredient5y = request.GET.get('ingredient5y', None)
    ingredient5n = request.GET.get('ingredient5n', None)
    keyword5 = request.GET.get('keyword5', None)
    ingredient1y = request.GET.get('ingredient1y', None)
    ingredient1n = request.GET.get('ingredient1n', None)
    keyword1 = request.GET.get('keyword1', None)

    if query:
        queryset = queryset.filter(name__iregex=query)
    if caloriesl:
        queryset = queryset.filter(bzy__calories__lte=caloriesl)
        queryset = queryset.annotate(text_len=Length('bzy__calories')).filter(text_len__lte=len(caloriesl))
    if proteinl:
        queryset = queryset.filter(bzy__protein__lte=proteinl)
        queryset = queryset.annotate(text_len=Length('bzy__protein')).filter(text_len__lte=len(proteinl))
    if fatsl:
        queryset = queryset.filter(bzy__fats__lte=fatsl)
        queryset = queryset.annotate(text_len=Length('bzy__calories')).filter(text_len__lte=len(fatsl))
    if carbohydratesl:
        queryset = queryset.filter(bzy__carbohydrates__lte=carbohydratesl)
        queryset = queryset.annotate(text_len=Length('bzy__carbohydrates')).filter(text_len__lte=len(carbohydratesl))
    if caloriesm:
        queryset = queryset.filter(bzy__calories__gte=caloriesm)
        queryset = queryset.annotate(text_len=Length('bzy__calories')).filter(text_len__gte=len(caloriesm))
    if proteinm:
        queryset = queryset.filter(bzy__protein__gte=proteinm)
        queryset = queryset.annotate(text_len=Length('bzy__protein')).filter(text_len__gte=len(proteinm))
    if fatsm:
        queryset = queryset.filter(bzy__fats__gte=fatsm)
        queryset = queryset.annotate(text_len=Length('bzy__fats')).filter(text_len__gte=len(fatsm))
    if carbohydratesm:
        queryset = queryset.filter(bzy__carbohydrates__gte=carbohydratesm)
        queryset = queryset.annotate(text_len=Length('bzy__carbohydrates')).filter(text_len__gte=len(carbohydratesm))
    if duration:
        queryset = queryset.filter(duration__lte=duration)
        queryset = queryset.annotate(text_len=Length(str('duration'))).filter(text_len__lte=len(str(duration)))
    if ingredient1y:
        queryset = queryset.filter(ingredientsOneString__iregex=ingredient1y)
    if ingredient1n:
        queryset = queryset.exclude(ingredientsOneString__iregex=ingredient1n)
    if keyword1:
        queryset = queryset.filter(description__iregex=keyword1)
    if ingredient2y:
        queryset = queryset.filter(ingredientsOneString__iregex=ingredient2y)
    if ingredient2n:
        queryset = queryset.exclude(ingredientsOneString__iregex=ingredient2n)
    if keyword2:
        queryset = queryset.filter(description__iregex=keyword2)
    if ingredient3y:
        queryset = queryset.filter(ingredientsOneString__iregex=ingredient3y)
    if ingredient3n:
        queryset = queryset.exclude(ingredientsOneString__iregex=ingredient3n)
    if keyword3:
        queryset = queryset.filter(description__iregex=keyword3)
    if ingredient4y:
        queryset = queryset.filter(ingredientsOneString__iregex=ingredient4y)
    if ingredient4n:
        queryset = queryset.exclude(ingredientsOneString__iregex=ingredient4n)
    if keyword4:
        queryset = queryset.filter(description__iregex=keyword4)
    if ingredient5y:
        queryset = queryset.filter(ingredientsOneString__iregex=ingredient5y)
    if ingredient5n:
        queryset = queryset.exclude(ingredientsOneString__iregex=ingredient5n)
    if keyword5:
        queryset = queryset.filter(description__iregex=keyword5)



    serializer = serializers.FilterSearchRecipeSerializer(queryset, many=True)
    return Response(serializer.data)
