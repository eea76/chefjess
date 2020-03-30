from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import MealForm

####################
# user views
####################

def index(request):
  meals = Meal.objects.all()


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



####################
# admin views
####################


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

  return render(request, 'new_meal.html', {'form': form})
