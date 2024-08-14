from django.urls import path
from .views import Home, LogoutDashboard, SignupView, Tasks, ListUserView, CreateUser, CreateUserView


urlpatterns = [
    path("home/", Home.as_view(), name="home"),
    path("logout/", LogoutDashboard.as_view(), name="logout"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("tasks/", Tasks.as_view(), name="tasks"),
    path("equipes_list/", ListUserView.as_view(), name="user_list_view"),
    path("equipes_create/", CreateUser.as_view(), name="user_create"),
    path("new_user/", CreateUserView.as_view(), name="user_create_view")
]