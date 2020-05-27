from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class MyUser(AbstractUser):
	display_name = models.CharField(max_length=50)

	# add additional fields in here

	def __str__(self):
		return self.username