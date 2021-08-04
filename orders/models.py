
from django.db import models

# Create your models here.
from django.db.models import signals
from django.dispatch import receiver

from food.models import Food
from profiles.models import Profile

PAYED_METHOD = [
    ('#1' ,'CASH'),
    ('#2' ,'WITH CREDIT CARD'),
]


class SelectedFood(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE ,related_name="profiles_selected_food")
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField()
    description = models.TextField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return str(self.food) + " | " + str(self.quantity) + "db : " + str(self.total_price)




@receiver(signals.pre_save ,sender=SelectedFood)
def calculate_select_food_total_price(sender ,instance ,**kwargs):
    price = int(instance.quantity) * instance.food.food_price
    print("*"*5,"receiver- quantity",instance.quantity," food price",instance.food.food_price,"price is:",price)
    print(type(price))
    instance.total_price = price



class Orders(models.Model):
    buyer = models.ForeignKey(Profile ,on_delete=models.CASCADE)
    ordered_foods = models.ManyToManyField(SelectedFood)
    total_price = models.IntegerField()
    deliver_location_city = models.CharField(max_length=100)
    deliver_location_street = models.CharField(max_length=100)
    deliver_location_zip = models.IntegerField()
    comment = models.TextField(blank=True)
    payed_method = models.CharField(max_length=2 ,choices=PAYED_METHOD)
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def get_ordered_foods(self):
        return self.ordered_foods.all()







