from django.db import models


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
  date = models.DateField()
  meal_type = models.ForeignKey(MealType, null=True, blank=True, on_delete=models.CASCADE)
  cuisine = models.ForeignKey(Cuisine, null=True, blank=True, on_delete=models.CASCADE)
  person = models.ManyToManyField(Person, null=True, blank=True)
  location = models.CharField(max_length=200, null=True, blank=True)
  notes = models.TextField(null=True, blank=True)
  make_again = models.BooleanField(default=True)

  def __str__(self):
    return self.meal_name


