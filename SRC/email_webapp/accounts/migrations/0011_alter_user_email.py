# Generated by Django 4.0.2 on 2022-02-22 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, error_messages={'unique': 'Ops tekrarie'}, max_length=254, null=True, unique=True, verbose_name='email address'),
        ),
    ]