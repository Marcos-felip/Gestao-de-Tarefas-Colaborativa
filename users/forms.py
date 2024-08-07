from allauth.account.forms import SignupForm
from django import forms

class OrganizationForm(SignupForm):
    name_organization = forms.CharField(max_length=100, required=False, label='Organização', widget=forms.TextInput(attrs={'placeholder': 'Nome da Organização/Empresa'})
    )

    field_order=["name_organization"]

