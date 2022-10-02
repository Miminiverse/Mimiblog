# Generated by Django 4.1.1 on 2022-09-25 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0008_todo_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='audio',
            field=models.FileField(default='default.mp3', upload_to='audio_files'),
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
    ]
