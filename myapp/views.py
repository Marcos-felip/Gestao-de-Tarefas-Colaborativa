from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

# Home do projeto
def login(request):
    return render(request, 'accounts/login.html')

# Pagina de registro
def registrar(request):
     return render(request, 'accounts/register.html')

