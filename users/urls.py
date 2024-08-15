from django.urls import path
from .views import Home, LogoutDashboard, SignupView, Tasks, ListUserView, CreateUserView, DeleteUserView


urlpatterns = [
    path("home/", Home.as_view(), name="home"),
    path("logout/", LogoutDashboard.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("tasks/", Tasks.as_view(), name="tasks"),
    path("equipes_list/", ListUserView.as_view(), name="user_list_view"),
    path("new_user/", CreateUserView.as_view(), name="user_create_view"),
    path("delete_user/<int:pk>", DeleteUserView.as_view(), name="user_delete_view"),
]
