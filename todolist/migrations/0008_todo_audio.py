# Generated by Django 4.1.1 on 2022-09-25 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0007_audio_remove_todo_audio'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='audio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todolist.audio'),
        ),
    ]
