# Generated by Django 5.0.7 on 2024-08-20 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_category_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
    ]
