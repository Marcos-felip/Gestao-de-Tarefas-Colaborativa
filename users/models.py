from django.db import models
from django.contrib.auth.models import AbstractUser


class Organization(models.Model):
    name = models.CharField(max_length=150, verbose_name="nome", blank=True, null=True)

    def __str__(self):
        return self.name


class UserProfile(AbstractUser):
    organizations = models.ManyToManyField(Organization, through="Membership")

    def __str__(self):
        return self.username


class Membership(models.Model):
    class Permission(models.TextChoices):
        OWNER = "owner", "Proprietario"
        ADMIN = "admin", "Administrador"
        USER = "user", "Colaborador"

    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    type_permission = models.CharField(
        max_length=10, choices=Permission.choices, default=Permission.ADMIN.value
    )

    is_active = models.BooleanField(
        default=True
    )  # Novo campo para controle de ativação

    def __str__(self):
        return (
            f"{self.user} - {self.organization} ({self.get_type_permission_display()})"
        )
