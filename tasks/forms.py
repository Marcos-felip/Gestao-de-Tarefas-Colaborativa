from django import forms
from .models import Task, Category, Comment

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 
                  'description', 
                  'status', 
                  'category', 
                  'assigned_to']
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all() 
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
        
class TaskFilterForm(forms.Form):
    status = forms.ChoiceField(
        choices=[('', 'Todos')] + list(Task.Status.choices),
        required=False,
        label='Status'
    )