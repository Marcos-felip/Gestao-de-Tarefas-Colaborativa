from django.contrib import admin
from .models import Task, Category, Comment


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'assigned_to', 'created_by', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'assigned_to__username', 'created_by__username')
    list_filter = ('status', 'category', 'assigned_to', 'created_by', 'created_at', 'updated_at')
    ordering = ('-created_at',)  # Ordena por data de criação, mais recentes primeiro
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
