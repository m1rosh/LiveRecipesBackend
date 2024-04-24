from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('id/<int:id>/', views.OneRecipeInfo.as_view()),
    path('main_page/', views.MainPageRecipeList.as_view()),
    path('all_recipes/', views.RecipeList.as_view()),
    path('desserts/', views.DessertsList.as_view()),
    path('garnish/', views.GarnishList.as_view()),
    path('drinks/', views.DrinksList.as_view()),
    path('first_dishes/', views.FirstDishList.as_view()),
    path('second_dishes/', views.SecondDishList.as_view()),
    path('salads/', views.SaladsList.as_view()),
    path('sauces/', views.SauceList.as_view()),
    path('bakery/', views.BakeryList.as_view()),
    path('harvesting/', views.HarvestingList.as_view()),
    path('snacks/', views.SnackList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)