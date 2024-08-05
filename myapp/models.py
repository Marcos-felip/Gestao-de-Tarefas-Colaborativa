from django.db import models

class Equipe (models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    