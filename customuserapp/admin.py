from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from customuserapp.forms import CustomUserCreationForm
from customuserapp.models import MyUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = MyUser
    list_display = ['email', 'username']


# Register your models here.
admin.site.register(MyUser, UserAdmin)