from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager






class CustomerManager(BaseUserManager):
	pass



class CustomUser(AbstractBaseUser):
	email = models.EmailField(verbose_name='Email Address', unique=True)
	username = models.CharField(verbose_name='User Name', max_length=255, unique=True)
	firstname = models.CharField(verbose_name='First Name', max_length=255)
	lastname = models.CharField(verbose_name='Last Name', max_length=255)
	phoneno = models.CharField(verbose_name='Phone No.')











