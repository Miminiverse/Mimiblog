# Generated by Django 4.1 on 2022-10-01 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0008_alter_todo_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='audio',
            field=models.FileField(null=True, upload_to='audio_files'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
