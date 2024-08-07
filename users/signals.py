from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Organization

@receiver(post_save, sender=User)
def create_organization(sender, instance, created, **kwargs):
    if created:
        Organization.objects.create(name=f'{instance.username}\'s Team', owner=instance)
