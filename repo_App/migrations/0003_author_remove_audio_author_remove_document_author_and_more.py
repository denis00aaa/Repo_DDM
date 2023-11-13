# Generated by Django 4.2.7 on 2023-11-11 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo_App', '0002_audio_date_document_date_image_date_video_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='audio',
            name='author',
        ),
        migrations.RemoveField(
            model_name='document',
            name='author',
        ),
        migrations.RemoveField(
            model_name='image',
            name='author',
        ),
        migrations.RemoveField(
            model_name='video',
            name='author',
        ),
        migrations.AddField(
            model_name='audio',
            name='authors',
            field=models.ManyToManyField(to='repo_App.author'),
        ),
        migrations.AddField(
            model_name='document',
            name='authors',
            field=models.ManyToManyField(to='repo_App.author'),
        ),
        migrations.AddField(
            model_name='image',
            name='authors',
            field=models.ManyToManyField(to='repo_App.author'),
        ),
        migrations.AddField(
            model_name='video',
            name='authors',
            field=models.ManyToManyField(to='repo_App.author'),
        ),
    ]
