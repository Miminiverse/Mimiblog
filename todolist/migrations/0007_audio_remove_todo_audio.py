# Generated by Django 4.1.1 on 2022-09-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_todo_audio_alter_todo_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_title', models.CharField(max_length=64, null=True)),
                ('audio', models.FileField(default='default.mp3', upload_to='audio_files')),
            ],
        ),
        migrations.RemoveField(
            model_name='todo',
            name='audio',
        ),
    ]
