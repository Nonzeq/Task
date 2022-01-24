# Generated by Django 4.0.1 on 2022-01-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fist_name', models.CharField(max_length=128, verbose_name="Ім'я")),
                ('last_name', models.CharField(max_length=128, verbose_name='Фамілія')),
                ('email', models.EmailField(max_length=255, verbose_name='Пошта')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Публікація')),
            ],
        ),
    ]
