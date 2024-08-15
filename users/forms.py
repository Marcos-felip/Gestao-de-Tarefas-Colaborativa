from typing import Any
from allauth.account.forms import SignupForm
from .models import Organization, Membership, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import models


class OrganizationForm(SignupForm):
    name_organization = forms.CharField(
        max_length=100, 
        required=True,  
        label='Organização', 
        widget=forms.TextInput(attrs={'placeholder': 'Nome da Organização/Empresa'})
    )

    field_order = ["name_organization"]

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)

        # Cria ou obtém a organização
        organization_name = self.cleaned_data.get('name_organization')
        if organization_name:
            organization, created = Organization.objects.get_or_create(name=organization_name)
            # Cria ou atualiza o Membership
            membership, created = Membership.objects.get_or_create(
                user=user,
                organization=organization,
                defaults={'type_permission': Membership.Permission.OWNER.value}
            )
            if not created:
                membership.type_permission = Membership.Permission.OWNER.value
                membership.save()
        return user
    

class UserMemberForm(UserCreationForm):
    
    class Permission(models.TextChoices):
        Administrador = Membership.Permission.ADMIN
        Colaborador = Membership.Permission.USER
    
    email = forms.EmailField(required=True)
    
    # Herdando as opçoes que estão na classe Membership
    type_permission = forms.ChoiceField(
        choices=Permission.choices,
        required=True,
        widget=forms.Select,
        help_text="Tipo de Permissão do Usuario",
        label="Tipo de Permissão"
    )
    
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'type_permission')
        
    def __init__(self, *args: Any, **kwargs):
        super(UserMemberForm,self).__init__(*args, **kwargs)
        #self.fields['password2'].widget = forms.HiddenInput()
        del self.fields['password2']

        

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user