from django import forms
from .models import Meal, Recipe, Ingredient
# from tinymce import TinyMCE

# class TinyMCEWidget(TinyMCE):
#   def use_required_attribute(self, *args):
#     return False



class MealForm(forms.ModelForm):
  name = 'Meal'
  class Meta:
    model = Meal
    fields = ('meal_name',
      'cover',
      'date',
      'meal_type',
      'cuisine',
      'person',
      'location',
      'notes',
      'recipe',
      'make_again'
    )



class RecipeForm(forms.ModelForm):
  name = 'Recipe'
  class Meta:
    model = Recipe
    fields = ('recipe_name',
      'ingredient',
      'notes'
    )


class IngredientForm(forms.ModelForm):
  name = 'Ingredient'
  class Meta:
    model = Ingredient
    fields = ('ingredient_name',
      'notes'
    )

