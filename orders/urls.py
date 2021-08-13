from django.urls import path

from orders.views import SelectedFoodDeleteView, add_order_view, get_food_orders_view

app_name = "orders"
urlpatterns = [
    path('basket/', get_food_orders_view,name='food_order_view'),
    path('save/', add_order_view,name='save_order'),
    path("remove/<pk>/",SelectedFoodDeleteView.as_view(),name="remove_from_basket")

]