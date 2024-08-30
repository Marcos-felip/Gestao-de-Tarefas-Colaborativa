from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.signals import notify
from tasks.models import Comment, Task

@receiver(post_save, sender=Comment)
def notify_comment_creation(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        task = instance.task

        recipients = set()
        if user != task.created_by:
            recipients.add(task.created_by)
        if task.assigned_to and user != task.assigned_to:
            recipients.add(task.assigned_to)

        for recipient in recipients:
            notify.send(
                user,
                recipient=recipient,
                verb='comentou',
                target=task,  # Define a tarefa como o alvo da notificação
                description=f'{user} comentou na tarefa "{task.title}"'
            )
