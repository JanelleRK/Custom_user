from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
	display_name = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	age = models.IntegerField(default=0)