from django.contrib import admin

# Register your models here.
from orders.models import Orders, SelectedFood


class SelectedFoodAdmin(admin.ModelAdmin):
    list_display = ('pk', 'food', 'buyer', 'quantity', 'ordered', 'total_price', 'description')
    list_filter = ['buyer',]


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'approved', 'approved_time', 'total_price', 'deliver_location_street', 'payed_method')


admin.site.register(Orders, OrdersAdmin)
admin.site.register(SelectedFood, SelectedFoodAdmin)
