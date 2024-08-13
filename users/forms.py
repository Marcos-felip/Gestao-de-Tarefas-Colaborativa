from allauth.account.forms import SignupForm
from .models import Organization, Membership
from django import forms

class OrganizationForm(SignupForm):
    name_organization = forms.CharField(
        max_length=100, 
        required=True,  # Agora obrigatório
        label='Organização', 
        widget=forms.TextInput(attrs={'placeholder': 'Nome da Organização/Empresa'})
    )

    full_name = forms.CharField(
        max_length=100, 
        required=True, 
        label='Nome Completo',
        widget=forms.TextInput(attrs={'placeholder': 'Nome Completo'})
    )

    field_order = ["full_name", "name_organization"]

    def save(self, *args, **kwargs):
        user = super().save(*args, **kwargs)
        user.username = self.cleaned_data.get('full_name')
        user.save()

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
