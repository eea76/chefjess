from . import views, admin_views
from django.contrib.auth.decorators import login_required
from django.urls import path

urlpatterns = [

  # user urls
  path('', views.index, name='index'),
  path('meals', views.meals, name='meals'),
  path('meal/<int:id>/', views.meal_detail, name='meal_detail'),
  path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),


  # admin urls
  path('detect_browser/', admin_views.detect_browser, name='detect_browser'),
  path('meal/new/', admin_views.new_meal, name="new_meal"),
  path('post/<int:id>/edit/', admin_views.meal_edit, name='meal_edit'),
  path('person/new/', admin_views.new_person, name="new_person"),
  path('recipe/new/', admin_views.new_recipe, name="new_recipe"),
  path('ingredient/new/', admin_views.new_ingredient, name="new_ingredient"),

]
