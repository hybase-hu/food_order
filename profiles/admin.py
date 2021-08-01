from django.contrib import admin

# Register your models here.
from profiles.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'email')


admin.site.register(Profile, ProfileAdmin)
