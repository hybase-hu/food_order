from django.shortcuts import render, redirect
from django.views.generic import DeleteView
from food.models import Food
from orders.models import SelectedFood, PAYED_METHOD, Orders
from orders.utils import get_generate_uuid
from profiles.forms import ProfileForm
from profiles.models import Profile


def get_food_orders_view(request):
    print("1-------------")
    template_name = "orders/order.html"
    generate_uuid = get_generate_uuid(request)
    profile, created = Profile.objects.get_or_create(uuid=generate_uuid)

    if request.method == 'POST':
        food = Food.objects.get(pk=request.POST['pk'])
        print("2-------------")
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
        print("3-------------")
    context = {
        'basket_items': profile.get_selected_food(),
        'ordered_items': profile.get_under_order_food(),
        'total_price': profile.get_selected_food_total_price()
    }
    return render(request=request, context=context, template_name=template_name)


class SelectedFoodDeleteView(DeleteView):
    model = SelectedFood
    template_name = "orders/confirm.html"
    success_url = "/orders/basket/"


def this_food_is_ordered(profile):
    profile.get_selected_food().update(ordered=True)


def add_order_view(request):
    print("-------- add order view")
    template_name = "orders/saving_order.html"
    generate_uuid = get_generate_uuid(request)
    profile, created = Profile.objects.get_or_create(uuid=generate_uuid)
    saving_foods = profile.get_selected_food()
    profile_form = ProfileForm(instance=profile)


    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            print("*" * 5, request.POST)
            profile_form.save()
            payment_method = request.POST['payments']
            order_comment = request.POST['order_comment']

            orders, created = Orders.objects.get_or_create(
                buyer=profile,
                payed_method=payment_method,
                deliver_location_city=profile.deliver_location_city,
                deliver_location_street=profile.deliver_location_street,
                deliver_location_zip=profile.deliver_location_zip,
                total_price=profile.get_selected_food_total_price(),
                comment=order_comment
            )

            orders.ordered_foods.add(*saving_foods)

            print("*" * 5, "adding this foods for orders", saving_foods)
            print("this is created order?", created, orders, "foods:", orders.ordered_foods)
            this_food_is_ordered(profile)
            return redirect('food:foods_view')

    context = {
        "saving_foods": saving_foods,
        "profile": profile,
        'profile_form': profile_form,
        'payed_method': PAYED_METHOD,
    }

    return render(request=request, context=context, template_name=template_name)
