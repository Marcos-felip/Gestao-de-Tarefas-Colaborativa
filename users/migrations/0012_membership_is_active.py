# Generated by Django 5.0.7 on 2024-08-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_membership_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
