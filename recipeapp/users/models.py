from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import MyUserManager

class MyCustomUser(AbstractUser):

    username = None
    email = models.EmailField(max_length=225, unique=True)
    name = models.CharField(max_length=100)

    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['']
