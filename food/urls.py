from food.views import get_foods_with_type, FoodsView, ThisFoodView

app_name = "food"

from django.urls import path

urlpatterns = [
    path('food_type/<str:food_type>/', get_foods_with_type, name='this_type_foods_view'),
    path('food/<pk>', ThisFoodView.as_view(), name='get_this_food'),
    path('', FoodsView.as_view(), name='foods_view'),
]
