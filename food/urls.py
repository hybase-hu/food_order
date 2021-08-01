from food.views import FoodView

app_name = "food"

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', FoodView.as_view(),name='foods_view'),

]