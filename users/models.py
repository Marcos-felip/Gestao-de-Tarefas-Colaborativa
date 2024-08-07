from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):

    def __str__(self):
        return self.username


class Organization(models.Model):
     name = models.CharField(max_length=150, verbose_name='nome')

     def __str__(self):
         return self.name