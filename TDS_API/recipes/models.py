from django.db import models
from rest_framework.authtoken.admin import User


class Measurement_type(models.Model):
    measurement_types =[
        "Solide",
        "Liquide",
        "Both",
    ]
    measurement_type = models.CharField(blank=False, choices=measurement_types)

class Measurement(models.Model):
    measurement = models.CharField(max_length=100, blank=False)
    measurement_type = models.ForeignKey(Measurement_type, on_delete=models.SET_NULL)

class Categories_ingredients(models.Model):
    categories_ingredients = models.CharField(max_length=100, blank=False)

class Ingredients(models.Model):
    ingredient = models.CharField(max_length=100, blank=False)
    categories_ingredients = models.ForeignKey(Categories_ingredients, on_delete=models.SET_NULL)
    measurement_type = models.ForeignKey(Measurement_type, on_delete=models.SET_NULL)

class Difficulty(models.Model):
    difficulties =[
        "Facile",
        "Moyen",
        "Difficile",
    ]
    difficulty = models.CharField(max_length=100, blank=False, choices=difficulties)

class Diet(models.Model):
    diet = models.CharField(max_length=100, blank=False)

class Origins_recipes(models.Model):
    origins_recipes = models.CharField(max_length=100, blank=False)

class Categories_recipes(models.Model):
    categories_recipes = models.CharField(max_length=100, blank=False)

class Recipes(models.Model):
    name = models.CharField(max_length=100, blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(blank=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Categories_recipes, on_delete=models.SET_NULL, null=True)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.SET_NULL, null=True)
    diet = models.ForeignKey(Diet, on_delete=models.SET_NULL, null=True)
    origins = models.ForeignKey(Origins_recipes, on_delete=models.SET_NULL, null=True)

class Ingredients_recipes(models.Model):
    measure_quantity = models.FloatField(blank=False)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.SET_NULL, null=True)
    recipe = models.ForeignKey(Recipes, on_delete=models.SET_NULL, null=True)
    measurement = models.ForeignKey(Measurement, on_delete=models.SET_NULL, null=True)

class Img_recipes(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Kitchen_ustensiles(models.Model):
    kitchen_ustensile = models.CharField(max_length=100, blank=False)

class Kitchen_ustensile_recipe(models.Model):
    kitchen_ustensile = models.ForeignKey(Kitchen_ustensiles, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipes, on_delete=models.SET_NULL)

class Steps_recipes(models.Model):
    step = models.CharField(max_length=200, blank=False)
    number_of_steps = models.IntegerField(blank=False)
    recipe = models.ForeignKey(Recipes, on_delete=models.SET_NULL)

class Rates_recipes(models.Model):
    rate = models.FloatField(blank=False)
    comment = models.TextField(blank=False)
    posted_date = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Favorites_recipes(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
