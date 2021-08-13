from django import forms

from orders.models import Orders


class FoodOrdersUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FoodOrdersUpdateForm, self).__init__(*args, **kwargs)
        self.fields['expected_delivery_time'].widget = forms.DateInput(attrs={'type': 'datetime-local'})
        self.fields['approved'].required = True
        self.fields['expected_delivery_time'].required = True

    class Meta:
        model = Orders
        fields = ['approved', 'expected_delivery_time']
