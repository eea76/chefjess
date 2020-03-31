from . import views, admin_views
from django.contrib.auth.decorators import login_required
from django.urls import path

urlpatterns = [

  # user urls
  path('', views.index, name='index'),
  path('meal/<str:meal_type>/<int:id>/', views.meal_detail, name='meal_detail'),
  path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),


  # admin urls
  path('meal/new/', admin_views.new_meal, name="new_meal"),
  path('recipe/new/', admin_views.new_recipe, name="new_recipe"),
  path('ingredient/new/', admin_views.new_ingredient, name="new_ingredient"),

]
