from django.db import models
from rest_framework.authtoken.admin import User


class Measurement_type(models.Model):
    MEASUREMENT_TYPES = [
        ("solid", "Solide"),
        ("liquid", "Liquide"),
        ("both", "Both"),
    ]
    measurement_type = models.CharField(max_length=10, choices=MEASUREMENT_TYPES, blank=False, verbose_name="Type de mesure")

class Measurement(models.Model):
    measurement = models.CharField(max_length=100, blank=False, verbose_name="Mesure")
    measurement_type = models.ForeignKey(Measurement_type, on_delete=models.SET_NULL, null=True)

class Categories_ingredients(models.Model):
    categories_ingredients = models.CharField(max_length=100, blank=False, verbose_name="Catégorie de l'ingredient")

class Ingredients(models.Model):
    ingredient = models.CharField(max_length=100, blank=False, verbose_name="Ingrédient")
    categories_ingredients = models.ForeignKey(Categories_ingredients, on_delete=models.SET_NULL)
    measurement_type = models.ForeignKey(Measurement_type, on_delete=models.SET_NULL)

class Difficulty(models.Model):
    DIFFICULTIES = [
        ("facile", "Facile"),
        ("moyen", "Moyen"),
        ("difficile", "Difficile"),
    ]
    difficulty = models.CharField(max_length=10, choices=DIFFICULTIES, blank=False, verbose_name="Difficultée")

class Diet(models.Model):
    diet = models.CharField(max_length=100, blank=False, verbose_name="Régime alimentaire")

class Origins_recipes(models.Model):
    origins_recipes = models.CharField(max_length=100, blank=False, verbose_name="Origine de la recette")

class Categories_recipes(models.Model):
    categories_recipes = models.CharField(max_length=100, blank=False, verbose_name="Catégorie de la recette")

class Recipes(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="Nom")
    created_date = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(blank=False, verbose_name="Temps de préparation")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Categories_recipes, on_delete=models.SET_NULL, null=True)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.SET_NULL, null=True)
    diet = models.ForeignKey(Diet, on_delete=models.SET_NULL, null=True)
    origins = models.ForeignKey(Origins_recipes, on_delete=models.SET_NULL, null=True)

class Ingredients_recipes(models.Model):
    measure_quantity = models.FloatField(blank=False, verbose_name="Quantité")
    ingredient = models.ForeignKey(Ingredients, on_delete=models.SET_NULL, null=True)
    recipe = models.ForeignKey(Recipes, on_delete=models.SET_NULL, null=True)
    measurement = models.ForeignKey(Measurement, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ['ingredient', 'recipe']

class Img_recipes(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Kitchen_ustensiles(models.Model):
    kitchen_ustensile = models.CharField(max_length=100, blank=False, verbose_name="Ustensile de cuisine")

class Kitchen_ustensile_recipe(models.Model):
    kitchen_ustensile = models.ForeignKey(Kitchen_ustensiles, on_delete=models.CASCADE, related_name="recipes", verbose_name="Ustensile de cuisine")
    recipe = models.ForeignKey(Recipes, on_delete=models.SET_NULL, null=True, related_name="kitchen_ustensiles")

class Steps_recipes(models.Model):
    step = models.CharField(max_length=200, blank=False, verbose_name="Étape")
    number_of_steps = models.IntegerField(blank=False)
    recipe = models.ForeignKey(Recipes, on_delete=models.SET_NULL, null=True, related_name="steps")

class Rates_recipes(models.Model):
    rate = models.FloatField(blank=False, verbose_name="Note")
    comment = models.TextField(blank=False, verbose_name="Commentaire")
    posted_date = models.DateTimeField(auto_now_add=True)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Favorites_recipes(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

