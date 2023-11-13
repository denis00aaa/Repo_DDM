# Generated by Django 4.2.7 on 2023-11-05 20:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('size', models.FloatField()),
                ('theme', models.CharField(max_length=100)),
                ('up_date', models.DateField()),
                ('format', models.CharField(max_length=5)),
                ('duration', models.DurationField(verbose_name='')),
                ('file', models.FileField(upload_to='files/audios')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('size', models.FloatField()),
                ('theme', models.CharField(max_length=100)),
                ('up_date', models.DateField()),
                ('format', models.CharField(max_length=5)),
                ('Resumen', models.TextField(max_length=2000)),
                ('file', models.FileField(upload_to='files/documents')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('size', models.FloatField()),
                ('theme', models.CharField(max_length=100)),
                ('up_date', models.DateField()),
                ('format', models.CharField(max_length=5)),
                ('dimensions', models.CharField(max_length=15)),
                ('file', models.FileField(upload_to='files/images')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=250)),
                ('size', models.FloatField()),
                ('theme', models.CharField(max_length=100)),
                ('up_date', models.DateField()),
                ('format', models.CharField(max_length=5)),
                ('duration', models.IntegerField(verbose_name='')),
                ('file', models.FileField(upload_to='files/videos')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_professor', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
    ]
