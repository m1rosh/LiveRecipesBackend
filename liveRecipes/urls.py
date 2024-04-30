from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('id/<int:id>/', views.OneRecipeInfo.as_view(), name='one_recipe'),
    path('main_page/', views.MainPageRecipeList.as_view()),
    path('all_recipes/', views.RecipeList.as_view()),
    path('desserts/', views.DessertsList.as_view(), name='desserts'),
    path('garnish/', views.GarnishList.as_view(), name='garnish'),
    path('drinks/', views.DrinksList.as_view(), name='drinks'),
    path('first_dishes/', views.FirstDishList.as_view(), name='first_dishes'),
    path('second_dishes/', views.SecondDishList.as_view(), name='second_dishes'),
    path('salads/', views.SaladsList.as_view(), name='salads'),
    path('sauces/', views.SauceList.as_view(), name='sauces'),
    path('bakery/', views.BakeryList.as_view(), name='bakery'),
    path('harvesting/', views.HarvestingList.as_view(), name='harvesting'),
    path('snacks/', views.SnackList.as_view(), name='snacks'),
    path('queryset=<str:query>/', views.search, name='queryset'),
    path('recipes_feed/', views.recipes_feed, name='recipes_feed')
]

urlpatterns = format_suffix_patterns(urlpatterns)