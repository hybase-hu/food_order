# Create your views here.


from django.views.generic.list import ListView

from food.models import Food, FOOD_TYPE, get_food_with_type



class FoodView(ListView):
    model = Food
    template_name = 'food/food_list.html'


    def get_queryset(self):
        qs = get_food_with_type(food_type=FOOD_TYPE[0])
        print("qs is ",qs)
        print("type",FOOD_TYPE[0])
        return qs

