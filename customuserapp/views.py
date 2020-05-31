from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import logout

from customuserapp.forms import CreateCustomUserForm
from customuserapp.models import MyUser

# Create your views here.
def index(request):
	return render(request, 'index.html')


def sign_up_view(request):
	html = "signup.html"

	if request.method == "POST":
		form = CreateCustomUserForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			MyUser.objects.create(
				username=data['username'],
				email=data['email'],
				display_name=data['display_name'],
				password=data['password'],
				age = data['age']
			)
			return HttpResponseRedirect(reverse('homepage'))

	form = CreateCustomUserForm()

	return render(request, html, {"form": form})


def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('homepage'))