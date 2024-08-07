from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.CharField(max_length=255)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owned_team')
    members = models.ManyToManyField(User, related_name='teams')

    def __str__(self):
        return self.name
