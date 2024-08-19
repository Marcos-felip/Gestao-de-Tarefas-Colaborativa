from django.urls import path
from .views import Home, LogoutDashboard, SignupView, ListUserView, CreateUserView, EnableUserView, DisableUserView, DeleteUserView 


urlpatterns = [
    path("home/", Home.as_view(), name="home"),
    path("logout/", LogoutDashboard.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("equipes_list/", ListUserView.as_view(), name="user_list_view"),
    path("new_user/", CreateUserView.as_view(), name="user_create_view"),
    path("user/<int:pk>/delete/", DeleteUserView.as_view(), name="user_delete_view"),
    path('user/<int:pk>/enable/', EnableUserView.as_view(), name='user_enable_view'),
    path('user/<int:pk>/disable/', DisableUserView.as_view(), name='user_disable_view'),
]
