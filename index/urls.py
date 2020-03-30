from . import views
from django.contrib.auth.decorators import login_required
from django.urls import path

urlpatterns = [

  # user urls
  path('', views.index, name='index'),
  path('meal/<str:meal_type>/<int:id>/', views.meal_detail, name='meal_detail'),


  # admin urls
  path('meal/new/', views.new_meal, name="new_meal"),

]
