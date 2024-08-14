from allauth.account.forms import SignupForm
from .models import Organization, Membership, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django import forms

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
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user