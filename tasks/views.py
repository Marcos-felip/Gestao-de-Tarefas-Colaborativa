from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task, Category, Comment
from .forms import TaskForm, CategoryForm, CommentForm
from django.db.models import Q


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'

    def get_queryset(self):
        return Task.objects.filter(Q(created_by=self.request.user) | Q(assigned_to = self.request.user))


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/tasks_detail.html'
    

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/tasks_form.html'
    success_url = reverse_lazy('tasks_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/tasks_form.html'
    success_url = reverse_lazy('tasks_list')


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/tasks_confirm_delete.html'
    success_url = reverse_lazy('tasks_list') # redirecionamento para (Tarefas)


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'tasks/new_categories.html'
    success_url = reverse_lazy('tasks_create')  # Redireciona para a página de criação de tarefas ou outra página
    

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'tasks/tasks_detail.html'
    