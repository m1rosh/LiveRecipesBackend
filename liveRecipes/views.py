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
    queryset = Recipe.objects.all()
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