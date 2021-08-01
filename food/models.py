from django.db import models

# Create your models here.
from django.template.defaultfilters import upper

FOOD_TYPE = [
    ("#1", "Hamburger"),
    ("#2", "Pizza"),
    ("#3", "Other"),

]


def get_food_with_type(food_type):
    qs = []
    for obj in Food.objects.all():
        print(obj.food_type, food_type[0])
        if obj.food_type == food_type[0]:
            qs.append(obj)
    print(qs)
    return qs


class Food(models.Model):
    food_code = models.CharField(max_length=5,unique=True)
    food_name = models.CharField(max_length=150)
    food_pictures = models.ImageField(upload_to="food_image")
    food_description = models.TextField()
    food_price = models.IntegerField()
    food_type = models.CharField(choices=FOOD_TYPE, max_length=2)

    def __str__(self):
        return "[" + upper(self.food_code) + "] " + self.food_name + " - " + self.get_food_type_display()
