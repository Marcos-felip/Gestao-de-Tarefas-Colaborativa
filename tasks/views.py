from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from tasks.models import Task, Category, Comment
from users.models import Membership
from tasks.forms import TaskForm, CategoryForm, CommentForm, TaskFilterForm
from django.db.models import Q
from notifications.models import Notification 


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/tasks_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = Task.objects.filter(Q(created_by=self.request.user) | Q(assigned_to=self.request.user))
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskFilterForm(self.request.GET)
        return context
    

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/tasks_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(task=self.object).order_by('created_at')
        context['form'] = CommentForm()
        context['room_name'] = self.object.id  # Passa o ID da tarefa como room_name
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
