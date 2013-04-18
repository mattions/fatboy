from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    date_of_birth = models.DateField()
    height = models.FloatField()
    REQUIRED_FIELDS = ['date_of_birth', 'height']
    USERNAME_FIELD = 'username'
