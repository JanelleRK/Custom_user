from django import forms
from .models import MyUser


class CreateCustomUserForm(forms.ModelForm):
	class Meta:
		model = MyUser
		fields = [
			'username',
			'email',
            'display_name',
			'age'
		]