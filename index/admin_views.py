from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import MealForm, RecipeForm



@login_required
def new_meal(request):
  if request.method == 'POST':
    form = MealForm(request.POST)
    if form.is_valid():
      meal = form.save(commit=False)
      meal.save()
      form.save_m2m()
      return redirect('meal_detail', meal_type=meal.meal_type, id=meal.id)
  else:
    form = MealForm()

  return render(request, 'form.html', {'form': form})


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

  return render(request, 'form.html', {'form': form})
