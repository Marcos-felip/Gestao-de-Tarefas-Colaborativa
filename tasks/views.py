from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from tasks.models import Task, Category, Comment
from tasks.forms import TaskForm, CategoryForm, CommentForm
from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
import json


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'

    def get_queryset(self):
        return Task.objects.filter(Q(created_by=self.request.user) | Q(assigned_to = self.request.user))


class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/tasks_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()  # Obtém os comentários da tarefa
        context['form'] = CommentForm()  # Adiciona o formulário de comentário ao contexto
        # Passa o nome da tarefa como um contexto adicional
        context['room_name'] = self.object.title  # Supondo que o título da tarefa é o nome da sala
        return context


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



def room(request, room_name):
    return render(request, "tasks/tasks_detail.html", {
        "room_name_json": mark_safe(json.dumps(room_name)) 
    })