# Generated by Django 4.0.1 on 2022-01-24 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAPtask', '0006_alter_user_fist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='fist_name',
            field=models.CharField(max_length=128, verbose_name="Ім'я"),
        ),
    ]
