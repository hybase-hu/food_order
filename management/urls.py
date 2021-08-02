from django.urls import path

from management.views import FoodListView, FoodUpdateView, LoginUserView

app_name = "management"

urlpatterns = [
    path('login/', LoginUserView.as_view(), name="login"),
    path('food_list/', FoodListView.as_view(), name="management_food_list"),
    path('food_update/<pk>/', FoodUpdateView.as_view(), name="management_food_update"),

]
