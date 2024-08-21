# Generated by Django 5.0.7 on 2024-08-21 12:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_category_name'),
        ('users', '0013_userprofile_organizations'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='organization',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.organization'),
            preserve_default=False,
        ),
    ]
