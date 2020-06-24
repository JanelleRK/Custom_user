from django.contrib import admin
from django.urls import path
from customuserapp import views

urlpatterns = [
	path('', views.homepage_view, name='homepage'),
	path('login/', views.login_view, name='login'),
	path('signup/', views.sign_up_view, name='signup'),
	path('logout/', views.logout_view, name='logout'),

]
