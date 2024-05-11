from django.db import models


class Recipe(models.Model):
    name = models.TextField()
    bzy = models.JSONField()
    duration = models.IntegerField()
    photo = models.TextField()
    description = models.TextField()
    ingredients = models.JSONField()
    steps = models.JSONField()
    tag = models.ManyToManyField('Tag', related_name='recipes', null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    dish_type = models.CharField(max_length=255)

    def __str__(self):
        return self.dish_type
