from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import MealForm, RecipeForm, IngredientForm, PersonForm



@login_required
def new_meal(request):
  if request.method == 'POST':
    form = MealForm(request.POST, request.FILES)
    if form.is_valid():
      meal = form.save(commit=False)
      meal.save()
      form.save_m2m()
      return redirect('meal_detail', meal_type=meal.meal_type, id=meal.id)
  else:
    form = MealForm()

  obj = {
    'form': form
  }

  return render(request, 'form.html', obj)


@login_required
def new_person(request):
  if request.method == 'POST':
    form = PersonForm(request.POST)
    if form.is_valid():
      person = form.save(commit=False)
      person.save()
      return redirect('new_meal')
  else:
    form = PersonForm()

  obj = {
    'form': form
  }

  return render(request, 'form.html', obj)


@login_required
def new_recipe(request):
  if request.method == 'POST':
    form = RecipeForm(request.POST)
    if form.is_valid():
      recipe = form.save(commit=False)
      recipe.save()
      form.save_m2m()
      return redirect('recipe_detail', id=recipe.id)
  else:
    form = RecipeForm()

  obj = {
    'form': form
  }

  return render(request, 'form.html', obj)


@login_required
def new_ingredient(request):
  if request.method == 'POST':
    form = IngredientForm(request.POST)
    if form.is_valid():
      ingredient = form.save(commit=False)
      ingredient.save()
      return redirect('new_ingredient')
  else:
    form = IngredientForm()

  obj = {
    'form': form
  }

  return render(request, 'form.html', obj)
