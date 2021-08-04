from django.contrib import admin

# Register your models here.
from orders.models import Orders, SelectedFood

class SelectedFoodAdmin(admin.ModelAdmin):
    list_display = ('pk','food','buyer','quantity','ordered','total_price','description')

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('pk','total_price','deliver_location_street','payed_method')

admin.site.register(Orders,OrdersAdmin)
admin.site.register(SelectedFood,SelectedFoodAdmin)
