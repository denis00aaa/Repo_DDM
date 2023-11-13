from django.urls import path
from . import views

app_name = "repo_App"

urlpatterns = [
    # path('login/', views.signin, name='login'),
    #
    path('', views.home, name='home'),
    path('get_authors/', views.getAuthors, name='get_authors'),
    path('get_themes/', views.getThemes, name='get_themes'),

    path('documentos/', views.documents, name='documents'),

    path('videos/', views.videos, name='videos'),

    path('audios/', views.audios, name='audios'),

    path('imagenes/', views.images, name='images')
]