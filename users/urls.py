from django.urls import path
from .views import home

urlpatterns = [  
    path('home/', home.as_view(), name='home')
] 

