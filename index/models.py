from django.db import models
from django.utils import timezone

from django_resized import ResizedImageField
# https://github.com/un1t/django-resized


class Ingredient(models.Model):
  ingredient_name = models.CharField(max_length=200)
  notes = models.TextField(max_length=200, null=True, blank=True)

  def __str__(self):
    return self.ingredient_name


class Recipe(models.Model):
  recipe_name = models.CharField(max_length=200)
  ingredient = models.ManyToManyField(Ingredient, null=True, blank=True)
  notes = models.TextField(max_length=200, null=True, blank=True)

  def __str__(self):
    return self.recipe_name


class Person(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name


class MealType(models.Model):
  # lunch, dinner, breakfast, snack, dessert, misc
  meal_type = models.CharField(max_length=200)

  def __str__(self):
    return self.meal_type


class Cuisine(models.Model):
  # beef, chicken, seafood, vegetarian, etc
  cuisine = models.CharField(max_length=200)

  def __str__(self):
    return self.cuisine


class Meal(models.Model):
  meal_name = models.CharField(max_length=200, null=True, blank=True)
  # cover = models.ImageField(upload_to='images/', null=True)
  meal_image = ResizedImageField(size=[300, 300], crop=['middle', 'center'], upload_to='images/', null=True)
  date = models.DateField(default=timezone.now, null=True)
  meal_type = models.ForeignKey(MealType, null=True, blank=True, on_delete=models.CASCADE)
  cuisine = models.ForeignKey(Cuisine, null=True, blank=True, on_delete=models.CASCADE)
  person = models.ManyToManyField(Person, null=True, blank=True)
  location = models.CharField(max_length=200, null=True, blank=True)
  notes = models.TextField(null=True, blank=True)
  recipe = models.ForeignKey(Recipe, null=True, blank=True, on_delete=models.CASCADE)
  make_again = models.BooleanField(default=True)
  is_favorite = models.BooleanField(default=False, null=True)

  def __str__(self):
    return self.meal_name


