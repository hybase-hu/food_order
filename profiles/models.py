from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Profile(models.Model):
    email = models.EmailField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=150)
    full_name = models.CharField(max_length=150, blank=True)
    deliver_location_city = models.CharField(max_length=100, blank=True, null=True)
    deliver_location_street = models.CharField(max_length=100, blank=True, null=True)
    deliver_location_zip = models.IntegerField(blank=True, null=True)
    phone_number = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return self.uuid

    def get_selected_food(self):
        return self.profiles_selected_food.filter(ordered=False)
        # return self.profiles_selected_food.all()

    def get_under_order_food(self):
        return self.profiles_selected_food.filter(ordered=True)

    def get_selected_food_total_price(self):
        foods = self.get_selected_food()
        total_price = 0
        for food in foods:
            total_price += food.total_price
        return total_price
