import uuid

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import DeleteView

from food.models import Food
from orders.forms import OrderForm
from orders.models import SelectedFood
from orders.utils import get_generate_uuid
from profiles.forms import ProfileForm
from profiles.models import Profile


def food_orders_view(request):
    template_name = "orders/order.html"
    generate_uuid = get_generate_uuid(request)
    profile,created = Profile.objects.get_or_create(uuid=generate_uuid)
    if request.method == 'POST':
        food = Food.objects.get(pk=request.POST['pk'])
        this_selected_food = SelectedFood.objects.filter(buyer=profile, food=food).first()

        if this_selected_food is not None:
            this_selected_food.quantity = request.POST['food_count']
            this_selected_food.description = request.POST['food_comment']
            this_selected_food.save()
        else:
            this_selected_food = SelectedFood.objects.create(
                buyer=profile,
                food=food,
                description=request.POST['food_comment'],
                quantity=request.POST['food_count']
            )

    context = {
        'basket_items':profile.get_selected_food(),
        'total_price':profile.get_selected_food_total_price()
    }
    return render(request=request,context=context,template_name=template_name)


class SelectedFoodDeleteView(DeleteView):
    model = SelectedFood
    template_name = "orders/confirm.html"
    success_url = "/orders/"



def add_order_view(request):
    template_name = "orders/saving_order.html"
    generate_uuid = get_generate_uuid(request)
    profile, created = Profile.objects.get_or_create(uuid=generate_uuid)
    saving_foods = profile.get_selected_food()
    profile_form = ProfileForm(instance=profile)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST,instance=profile)
        if profile_form.is_valid():
            print("*"*5,profile_form.cleaned_data)
            profile_form.save()


    context = {
        "saving_foods": saving_foods,
        "profile": profile,
        'profile_form': profile_form,
    }

    return render(request=request,context=context,template_name=template_name)
