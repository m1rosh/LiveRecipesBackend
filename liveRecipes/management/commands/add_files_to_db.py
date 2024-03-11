from django.core.management.base import BaseCommand
import json
from liveRecipes.models import *

class Command(BaseCommand):
    help = 'disp hello'

    """def add_arguments(self, parser):
        parser.add_argument("num", type=int)"""
    tags = ['dessert', 'garnish', 'drink', 'firstDish', 'salad',
            'sauce', 'secondDish', 'bakery', 'harvesting', 'snack'
            ]
    for tag in tags:
        t = Tag(dish_type=tag)
        t.save()
    def handle(self, *args, **kwargs):
        self.stdout.write(str('running'))

        with open('data/deserty.json') as f:
            data = json.load(f)

        for recipe in data['all_recipes']:

            one_recipe = Recipe.objects.create(**recipe)
            one_recipe.tag.add(Tag.objects.get(dish_type='dessert'))
            one_recipe.save()

        with open('data/garniry.json') as f:
            data = json.load(f)

        for recipe in data['all_recipes']:

            one_recipe = Recipe.objects.create(**recipe)
            one_recipe.tag.add(Tag.objects.get(dish_type='garnish'))
            one_recipe.save()

        with open('data/napitki.json') as f:
            data = json.load(f)

        for recipe in data['all_recipes']:

            one_recipe = Recipe.objects.create(**recipe)
            one_recipe.tag.add(Tag.objects.get(dish_type='drink'))
            one_recipe.save()
        with open('data/pervye-bliuda.json') as f:
            data = json.load(f)

        for recipe in data['all_recipes']:

            one_recipe = Recipe.objects.create(**recipe)
            one_recipe.tag.add(Tag.objects.get(dish_type='firstDish'))
            one_recipe.save()
        with open('data/salaty.json') as f:
            data = json.load(f)

        for recipe in data['all_recipes']:

            one_recipe = Recipe.objects.create(**recipe)
            one_recipe.tag.add(Tag.objects.get(dish_type='salad'))
            one_recipe.save()
        with open('data/sousy-i-marinady.json') as f:
            data = json.load(f)

        for recipe in data['all_recipes']:

            one_recipe = Recipe.objects.create(**recipe)
            one_recipe.tag.add(Tag.objects.get(dish_type='sauce'))
            one_recipe.save()
        with open('data/vtorye-bliuda.json') as f:
            data = json.load(f)

        for recipe in data['all_recipes']:

            one_recipe = Recipe.objects.create(**recipe)
            one_recipe.tag.add(Tag.objects.get(dish_type='secondDish'))
            one_recipe.save()

        with open('data/vypechka.json') as f:
            data = json.load(f)

        for recipe in data['all_recipes']:

            one_recipe = Recipe.objects.create(**recipe)
            one_recipe.tag.add(Tag.objects.get(dish_type='bakery'))
            one_recipe.save()

        with open('data/zagotovki.json') as f:
            data = json.load(f)

        for recipe in data['all_recipes']:

            one_recipe = Recipe.objects.create(**recipe)
            one_recipe.tag.add(Tag.objects.get(dish_type='harvesting'))
            one_recipe.save()

        with open('data/zakuski.json') as f:
            data = json.load(f)

        for recipe in data['all_recipes']:

            one_recipe = Recipe.objects.create(**recipe)
            one_recipe.tag.add(Tag.objects.get(dish_type='snack'))
            one_recipe.save()


