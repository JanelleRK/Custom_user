from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from customuser.settings import AUTH_USER_MODEL

from customuserapp.forms import CreateCustomUserForm, LoginForm
from customuserapp.models import MyUser

# Create your views here.

def homepage_view(request):
	html='homepage.html'
	data=MyUser.objects.all()

	return render(request, html, {'data': data, 'auth_user': AUTH_USER_MODEL})


def sign_up_view(request):
	html = "signup.html"
	form=CreateCustomUserForm()

	if request.method == "POST":
		form = CreateCustomUserForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			new_user = MyUser.objects.create(
				username=data['username'],
				display_name=data['display_name'],
				password=data['password'],
			)
			new_user.save()
			login(request, new_user)
			return HttpResponseRedirect(reverse('homepage'))

	form = CreateCustomUserForm()

	return render(request, html, {"form": form})


def login_view(request):
	html = 'login.html'
	form = None
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			user = authenticate(request,
				username = data['username'],
				password = data['password'],
			)
			if user:
				login(request, user)
				return HttpResponseRedirect(request.GET.get('next', reverse('homepage'))
				)

	form = LoginForm()
	return render(request, html, { 'form': form })


def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('homepage'))