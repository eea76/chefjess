from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def index(request):
  meals = Meal.objects.all()
  people = Person.objects.all()


  obj = {
    'meals' : meals,
    'people' : people,

  }

  return render(request, 'index.html', obj)
