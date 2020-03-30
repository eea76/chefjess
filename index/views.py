from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse




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


@login_required
def new_meal(request):
  if request.method == 'POST':
    form = NewForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.save()
      form.save_m2m()
      return redirect('meal_detail')
  else:
    form = MealForm()


  return render(request, 'index/new_meal.html', {'form': form})
