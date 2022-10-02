# Generated by Django 4.1.1 on 2022-09-25 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_todo_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='audio',
            field=models.FileField(default='default.mp3', upload_to='audio_files'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='text',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
