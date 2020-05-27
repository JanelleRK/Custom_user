from django.contrib import admin
from django.urls import path
from customuserapp.views import index, sign_up_view, logout_view

urlpatterns = [
    path('', index, name='homepage'),
	path('signup/', sign_up_view),
	path('logout/', logout_view)
]
