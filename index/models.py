import uuid

import os

from functools import partial
from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

from django_resized import ResizedImageField
# https://github.com/un1t/django-resized


class Browser(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class OperatingSystem(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class PageLoad(models.Model):
    page = models.CharField(max_length=1000, null=True, blank=True)
    time_stamp = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=100, blank=True, null=True)
    browser = models.ForeignKey(Browser, blank=True, null=True, on_delete=models.CASCADE)
    operating_system = models.ForeignKey(OperatingSystem, blank=True, null=True, on_delete=models.CASCADE)
    meal = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.page


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


'''
the following two functions do some magic to change the uploaded file in the
Meal class to a uuid instead of the generic 'image' filename that iphones use.
There has to be a better way to do this (besides putting each image in its
own uuid-named folder within the bucket. That's insanity. Also this doesn't
do anything about file extensions. I'll work on that.
This might help: https://stackoverflow.com/questions/2680391/)
'''
def _update_filename(instance, filename, path):
    path = path
    filename = str(uuid.uuid4())
    print("-------")
    print(f"this image's file name is {filename}")
    print("-------")

    return os.path.join(path, filename)

def upload_to(path):
    return partial(_update_filename, path=path)


class Meal(models.Model):
    meal_name = models.CharField(max_length=200, null=True, blank=True)
    # cover = models.ImageField(upload_to='images/', null=True)
    meal_image = ResizedImageField(size=[300, 300], crop=['middle', 'center'], upload_to=upload_to("images/"), null=True)
    date = models.DateField(default=timezone.now, null=True)
    meal_type = models.ForeignKey(MealType, null=True, blank=True, on_delete=models.CASCADE)
    cuisine = models.ForeignKey(Cuisine, null=True, blank=True, on_delete=models.CASCADE)
    person = models.ManyToManyField(Person, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    recipe = models.ForeignKey(Recipe, null=True, blank=True, on_delete=models.CASCADE)
    make_again = models.BooleanField(default=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.meal_name


class Images (models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    image = ResizedImageField(size=[300, 300], crop=['middle', 'center'], upload_to=upload_to("images/"), null=True, blank=True)

    def __str__(self):
        return self.meal.meal_name
