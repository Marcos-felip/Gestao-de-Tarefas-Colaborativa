# Generated by Django 5.0.7 on 2024-08-22 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_alter_comment_content_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='title',
        ),
    ]
