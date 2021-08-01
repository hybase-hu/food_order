from django.urls import path

from orders.views import food_orders_view, SelectedFoodDeleteView, add_order_view

app_name = "orders"
urlpatterns = [
    path('', food_orders_view,name='foods_view'),
    path('save/', add_order_view,name='save_order'),
    path("remove/<pk>/",SelectedFoodDeleteView.as_view(),name="remove_from_basket")

]