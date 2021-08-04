from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from django.views.generic import UpdateView, ListView

from food.models import Food
from orders.models import Orders


def is_manager_members(user):
    return user.groups.filter(name="manager").exists()


class LoginUserView(LoginView):
    template_name = "management/login.html"
    model = User


class FoodListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    def test_func(self):
        return is_manager_members(self.request.user)

    login_url = '/management/login'
    redirect_field_name = '/management/management_food_list'
    model = Food
    template_name = 'management/food_list.html'


class FoodUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return is_manager_members(self.request.user)

    login_url = '/management/login'
    redirect_field_name = '/management/management_food_update'
    model = Food
    fields = ['food_code', 'food_name', 'food_pictures', 'food_description', 'food_price', 'food_type']
    template_name = "management/food_update.html"
    success_url = "/management/food_list"


class FoodOrdersView(LoginRequiredMixin, UserPassesTestMixin, ListView):

    def test_func(self):
        return is_manager_members(self.request.user)

    login_url = '/management/login'
    redirect_field_name = '/management/orders'
    success_url = '/management/orders'
    template_name = "management/orders.html"
    model = Orders

    def get_queryset(self):
        return Orders.objects.filter(approved=False)


class FoodOrdersUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return is_manager_members(self.request.user)

    login_url = '/management/login'
    redirect_field_name = '/management/management_orders'
    model = Orders
    fields = ['approved']

    template_name = "management/orders_update.html"
    success_url = "/management/food_list"
