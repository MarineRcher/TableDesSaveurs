from rest_framework import serializers
from .models import Recipes, Ingredients_recipes, Steps_recipes, Img_recipes, Kitchen_ustensile_recipe

class IngredientsRecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients_recipes
        fields = ['measure_quantity', 'ingredient', 'measurement']

class StepsRecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steps_recipes
        fields = ['step', 'number_of_steps']

class ImgRecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Img_recipes
        fields = ['name', 'posted_date']

class KitchenUstensileRecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitchen_ustensile_recipe
        fields = ['kitchen_ustensile']

class RecipesSerializer(serializers.ModelSerializer):
    ingredients = IngredientsRecipesSerializer(many=True)
    steps = StepsRecipesSerializer(many=True)
    images = ImgRecipesSerializer(many=True, required=False)
    kitchen_ustensiles = KitchenUstensileRecipeSerializer(many=True)

    class Meta:
        model = Recipes
        fields = ['name', 'duration', 'category', 'difficulty', 'diet', 'origins', 'ingredients', 'steps', 'images', 'kitchen_ustensiles']

    def create(self, validated_data):
        # Extract nested related data
        ingredients_data = validated_data.pop('ingredients')
        steps_data = validated_data.pop('steps')
        images_data = validated_data.pop('images', [])
        kitchen_ustensiles_data = validated_data.pop('kitchen_ustensiles')

        # Create the recipe instance
        recipe = Recipes.objects.create(**validated_data)

        # Create related models (Ingredients, Steps, etc.)
        for ingredient in ingredients_data:
            Ingredients_recipes.objects.create(recipe=recipe, **ingredient)

        for step in steps_data:
            Steps_recipes.objects.create(recipe=recipe, **step)

        for image in images_data:
            Img_recipes.objects.create(recipe=recipe, **image)

        for ustensile in kitchen_ustensiles_data:
            Kitchen_ustensile_recipe.objects.create(recipe=recipe, **ustensile)

        return recipe
