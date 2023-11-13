from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_professor = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Author(models.Model):
    name = models.CharField(max_length=250)

class Theme(models.Model):
    name = models.CharField(max_length=250)

class File(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    size = models.FloatField()
    date = models.DateField(null=True)
    up_date = models.DateTimeField(auto_now_add=True)
    format = models.CharField(max_length=5)
    authors = models.ManyToManyField(Author)
    themes = models.ManyToManyField(Theme)

    class Meta:
        abstract = True

class Document(File):
    resumen = models.TextField(max_length=2000)
    file = models.FileField(upload_to="files/documents")

class Video(File):
    duration = models.IntegerField(_(""))
    file = models.FileField(upload_to="files/videos")

class Audio(File):
    duration = models.DurationField(_(""))
    file = models.FileField(upload_to="files/audios")

class Image(File):
    dimensions = models.CharField(max_length=15)
    file = models.FileField(upload_to="files/images")
