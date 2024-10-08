# Generated by Django 5.0.7 on 2024-08-12 19:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_organization_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='organizations',
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='nome'),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_permission', models.CharField(choices=[('owner', 'Proprietario'), ('admin', 'Administrador')], default='admin', max_length=10)),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.organization')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
