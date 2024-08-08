from django.db import models 
from django.contrib.auth.models import AbstractUser


class Organization(models.Model):
     name = models.CharField(max_length=150, verbose_name='nome', default='Default Organization Name')

     def __str__(self):
         return self.name

class UserProfile(AbstractUser):
    organizations = models.ManyToManyField(Organization, blank=True, related_name='users')

    def __str__(self):
        return self.username