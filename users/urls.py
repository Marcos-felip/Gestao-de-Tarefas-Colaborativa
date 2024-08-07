from django.urls import path
from .views import home, logoutDashboard

urlpatterns = [  
    path('home/', home.as_view(), name='home'),
    path("logout/", logoutDashboard.as_view(), name="logout")
] 

