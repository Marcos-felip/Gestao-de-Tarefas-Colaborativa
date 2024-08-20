from django.urls import path
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, CategoryCreateView

urlpatterns = [
    path('task/', TaskListView.as_view(), name='tasks_list'),
    path('task/<int:pk>/detail/', TaskDetailView.as_view(), name='tasks_detail'),
    path('task/new/', TaskCreateView.as_view(), name='tasks_create'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='tasks_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='tasks_delete'),
    path('create_category/', CategoryCreateView.as_view(), name='create_category'),
    ]
