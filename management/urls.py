from django.urls import path

from management.views import FoodListView, FoodUpdateView, LoginUserView, FoodOrdersView, FoodOrdersUpdateView

app_name = "management"

urlpatterns = [
    path('', FoodListView.as_view(), name="management_food_list"),
    path('login/', LoginUserView.as_view(), name="login"),
    path('food_update/<pk>/', FoodUpdateView.as_view(), name="management_food_update"),
    path('orders/', FoodOrdersView.as_view(), name="management_orders"),
    path('orders/<pk>/', FoodOrdersUpdateView.as_view(), name="management_orders_update"),

]
