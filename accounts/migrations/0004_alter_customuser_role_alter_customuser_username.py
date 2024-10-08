# Generated by Django 4.2 on 2024-08-24 17:05

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('operator', 'Operator'), ('member', 'Member')], default='member', max_length=10, verbose_name='role'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='user__d1bf2051', error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
