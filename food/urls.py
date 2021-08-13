from food.views import get_foods_with_type, FoodsView

app_name = "food"

from django.urls import path

urlpatterns = [

    path('', FoodsView.as_view(), name='foods_view'),
    path('<str:food_type>/', get_foods_with_type, name='this_type_foods_view'),

]
