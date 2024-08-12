from allauth.account.forms import SignupForm
from .models import Organization, Membership
from django import forms


class OrganizationForm(SignupForm):
    name_organization = forms.CharField(
        max_length=100, 
        required=False, 
        label='Organização', 
        widget=forms.TextInput(attrs={'placeholder': 'Nome da Organização/Empresa'})
    )

    field_order=["name_organization"]

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        organization_name = self.cleaned_data.get('name_organization')
        if organization_name:
            # Cria uma nova organização
            organization = Organization.objects.create(name=organization_name)
            # Associa a organização ao usuário
            user.organizations = organization
            user.save()
            # Cria um novo Membership para o usuário como proprietário
            Membership.objects.create(user=user,organization=organization, type_permission=Membership.Permission.OWNER.value)
        return user

