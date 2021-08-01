from django import forms
from phonenumber_field.formfields import PhoneNumberField

from profiles.models import Profile


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].required = True
        self.fields['email'].required = True
        self.fields['deliver_location_city'].required = True
        self.fields['deliver_location_zip'].required = True
        self.fields['phone_number'].required = True

    class Meta:
        model = Profile
        fields = [
            'full_name',
            'email',
            'deliver_location_city',
            'deliver_location_street',
            'deliver_location_zip',
            'phone_number',
        ]
