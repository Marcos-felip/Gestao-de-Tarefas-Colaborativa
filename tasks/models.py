from django.db import models
from users.models import UserProfile


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='Nome da Categoria')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        
        
class Task(models.Model):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pendente'
        IN_PROGRESS = 'in_progress', 'Em Progresso'
        COMPLETED = 'completed', 'Concluída'

    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(blank=True, null=True, verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING, verbose_name='Status')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks', verbose_name='Categoria')
    assigned_to = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks_assigned', verbose_name='Atribuído a')
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='tasks_created', verbose_name='Criado por')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tarefa'
        

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments', verbose_name='Tarefa')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Usuário')
    content = models.TextField(verbose_name='Conteúdo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')

    def __str__(self):
        return f"Comentário {self.content} de {self.user} em {self.task}"

    class Meta:
        verbose_name = 'Comentário'
        ordering = ['created_at']
