from django import forms
from .models import Meal, Recipe, Ingredient, Person
# from tinymce import TinyMCE

# class TinyMCEWidget(TinyMCE):
#   def use_required_attribute(self, *args):
#     return False



class MealForm(forms.ModelForm):
  title = 'Meal'
  class Meta:
    model = Meal
    fields = ('meal_name',
      'meal_image',
      'date',
      'meal_type',
      'cuisine',
      'person',
      'location',
      'notes',
      # 'recipe',
      'make_again',
      'is_favorite',
    )


class PersonForm(forms.ModelForm):
  title = 'Person'

  class Meta:
    model = Person
    fields = ('name',)



class RecipeForm(forms.ModelForm):
  title = 'Recipe'
  class Meta:
    model = Recipe
    fields = ('recipe_name',
      'ingredient',
      'notes'
    )


class IngredientForm(forms.ModelForm):
  title = 'Ingredient'
  class Meta:
    model = Ingredient
    fields = ('ingredient_name',
      'notes'
    )

