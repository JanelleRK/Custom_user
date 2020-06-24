from django.contrib import admin
from django.urls import path
from customuserapp import views

urlpatterns = [
    path('', views.index, name='homepage'),
	path('signup/', views.sign_up_view, name='signup'),
	path('logout/', views.logout_view, name='logout')
]
