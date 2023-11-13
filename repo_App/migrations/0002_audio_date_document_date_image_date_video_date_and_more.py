# Generated by Django 4.2.7 on 2023-11-11 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='audio',
            name='up_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='up_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='up_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='up_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
