from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

def index(request):

    return render(request, 'index.html')


def meals(request):
    meals = Meal.objects.all().order_by('-date')

    obj = {
        'meals': meals,
    }

    return render(request, 'meals.html', obj)


def meal_detail(request, id):
    meal = get_object_or_404(Meal, id=id)

    next_meal = Meal.objects.filter(date__gt=meal.date, date__isnull=False).order_by('date').first()
    prev_meal = Meal.objects.filter(date__lt=meal.date, date__isnull=False).order_by('-date').first()

    obj = {
        'meal': meal,
        'next_meal': next_meal,
        'prev_meal': prev_meal,
    }

    return render(request, 'meal_detail.html', obj)


def about_me(request):
    return render(request, 'about_me.html')


def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    obj = {
        'recipe': recipe
    }

    return render(request, 'recipe_detail.html', obj)


