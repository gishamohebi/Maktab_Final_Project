# Generated by Django 4.0.2 on 2022-02-22 14:57

import accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True, validators=[accounts.validators.valid_email]),
        ),
    ]