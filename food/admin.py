from django.contrib import admin

# Register your models here.
from food.models import Food

class FoodAdmin(admin.ModelAdmin):
    list_display = ('pk','food_name')

admin.site.register(Food,FoodAdmin)
