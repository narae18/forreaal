# Generated by Django 4.1.7 on 2023-08-18 00:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='post/')),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('event_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TTSAudio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('audio_file', models.FileField(upload_to='tts/')),
            ],
        ),
        migrations.CreateModel(
            name='TTSAudioTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_message', models.TextField()),
                ('audio_file', models.FileField(upload_to='tts_title/')),
            ],
        ),
    ]
