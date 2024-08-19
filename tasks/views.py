from django.views.generic import TemplateView

class Tasks(TemplateView):
    template_name = "tasks/tasks.html"  # redirecionamento para (Tarefas)
