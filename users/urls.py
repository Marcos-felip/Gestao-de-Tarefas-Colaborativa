from django.urls import path
from .views import Home, LogoutDashboard, SignupView, Tarefas, UserManage


urlpatterns = [  
    path('home/', Home.as_view(), name='home'),
    path("logout/", LogoutDashboard.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("tarefas/" , Tarefas.as_view(), name="tarefas"),
    path('equipe/', UserManage.as_view(), name='user_list')
] 

