from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import logout

from customuserapp.forms import CreateCustomUserForm, LoginForm
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
			)
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
			user = authenticate(
				username = data['username'],
				password = data['password'],
			)
			if user:
				login(request, user)
				return HttpResponseRedirect(request.GET.get('next', reverse('homepage'))
				)


def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('homepage'))