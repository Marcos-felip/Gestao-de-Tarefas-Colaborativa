# Generated by Django 5.0.7 on 2024-08-20 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_remove_category_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Nome da Categoria'),
        ),
    ]
