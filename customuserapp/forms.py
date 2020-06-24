from django import forms
from .models import MyUser


class CreateCustomUserForm(forms.ModelForm):
	class Meta:
		model = MyUser
		fields = [
			'username',
            'display_name',
			'password',
		]


class LoginForm(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(widget=forms.PasswordInput())