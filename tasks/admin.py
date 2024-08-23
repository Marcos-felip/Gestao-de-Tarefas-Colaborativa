from django.contrib import admin
from .models import Task, Category, Comment


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'assigned_to', 'created_by', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'assigned_to__username', 'created_by__username')
    list_filter = ('status', 'category', 'assigned_to', 'created_by', 'created_at', 'updated_at')
    ordering = ('-created_at',)  
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'content', 'created_at')
    list_filter = ('task', 'user')
    search_fields = ('content',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',) 
    