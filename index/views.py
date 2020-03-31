from .models import *
from django.shortcuts import render, get_object_or_404, redirect



def index(request):
  meals = Meal.objects.all().order_by('-date')


  obj = {
    'meals': meals,

  }

  return render(request, 'index.html', obj)


def meal_detail(request, meal_type, id):
  meal = get_object_or_404(Meal, id=id)

  obj = {
    'meal': meal
  }

  return render(request, 'meal_detail.html', obj)


def recipe_detail(request, id):
  recipe = get_object_or_404(Recipe, id=id)

  obj = {
    'recipe': recipe
  }

  return render(request, 'recipe_detail.html', obj)


