from django.urls import path

from management.views import FoodListView, FoodUpdateView, LoginUserView, FoodOrdersView, FoodOrdersUpdateView, \
    get_new_orders_json, FoodCreateView

app_name = "management"

urlpatterns = [
    path('', FoodListView.as_view(), name="management_food_list"),
    path('login/', LoginUserView.as_view(), name="login"),
    path('food_update/<pk>/', FoodUpdateView.as_view(), name="management_food_update"),
    path('orders/', FoodOrdersView.as_view(), name="management_orders"),
    path('create/', FoodCreateView.as_view(), name="management_create_food"),
    path('orders/json/', get_new_orders_json, name="management_orders_json"),
    path('orders/<pk>/', FoodOrdersUpdateView.as_view(), name="management_orders_update"),

]
