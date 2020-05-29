from django.contrib import admin

from index.models import *


class PageLoadAdmin(admin.ModelAdmin):
    list_filter = ('ip_address', 'meal')
    list_display = ('meal', 'time_stamp', 'page',)


admin.site.register(MealType)
admin.site.register(Person)
admin.site.register(Cuisine)
admin.site.register(Meal)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(PageLoad, PageLoadAdmin)




