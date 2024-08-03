from django.http import HttpResponse
from django.shortcuts import render

# Home do projeto
def login(request):
    return render(request, 'accounts/login.html')

