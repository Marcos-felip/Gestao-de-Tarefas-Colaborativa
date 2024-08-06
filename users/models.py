from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Organization(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='owned_organizations')
    members = models.ManyToManyField(UserProfile, related_name='organizations')
