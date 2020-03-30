from django.contrib import admin

from index.models import *

admin.site.register(MealType)
admin.site.register(Person)
admin.site.register(Cuisine)
admin.site.register(Meal)
admin.site.register(Ingredient)
admin.site.register(Recipe)

