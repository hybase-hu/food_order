# Create your views here.

from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView

from food.models import Food, FOOD_TYPE


class FoodsView(ListView):
    model = Food
    template_name = 'food/food_list.html'

    def get_queryset(self):
        # qs = get_food_with_type(food_type=FOOD_TYPE[0])
        qs = Food.objects.all()
        return qs

class ThisFoodView(DetailView):
    model = Food
    template_name = "food/food_view.html"

def get_foods_with_type(request, food_type):
    print("food type:", food_type)
    template_name = 'food/food_list.html'

    for t in FOOD_TYPE:
        print(t)
        if t[0] == food_type:
            food_type = t

    context = {
        'object_list': Food.objects.filter(food_type=food_type[0]),
    }
    print("context", context['object_list'])
    return render(request=request, context=context, template_name=template_name)
    # return HttpResponse()
