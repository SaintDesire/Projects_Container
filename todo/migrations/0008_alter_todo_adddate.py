# Generated by Django 4.2.7 on 2023-11-07 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_alter_todo_adddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='addDate',
            field=models.DateTimeField(null=True),
        ),
    ]
