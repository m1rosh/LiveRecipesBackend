from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

tags_encoding = {1: 'dessert', 2: 'garnish', 3: 'drink', 4: 'firstDish', 5: 'salad',
                 6: 'sauce', 7: 'secondDish', 8: 'bakery', 9: 'harvesting', 10: 'snack'}


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['tag'] = tags_encoding[representation['tag'][0]]
        return representation


class MainPageRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'duration', 'photo', 'tag']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['tag'] = tags_encoding[representation['tag'][0]]
        return representation
