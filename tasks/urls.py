from django.urls import path
from .views import Tasks

urlpatterns = [
    path("tasks/", Tasks.as_view(), name="tasks"),
]
