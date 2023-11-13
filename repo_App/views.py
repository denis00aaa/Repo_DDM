from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.core.paginator import Paginator


# Create your views here.
def getAuthors(request):
    authors = Author.objects.all()
    paginator = Paginator(authors, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    authors_list = [{'id': author.id, 'name': author.name} for author in page_obj]

    return JsonResponse({'authors': authors_list,
                         'has_previous': page_obj.has_previous(),
                         'has_next': page_obj.has_next(),
                         'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
                         'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
                         })


def getThemes(request):
    themes = Theme.objects.all()
    paginator = Paginator(themes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    themes_list = [{'id': theme.id, 'name': theme.name} for theme in page_obj]

    return JsonResponse({'themes': themes_list,
                         'has_previous': page_obj.has_previous(),
                         'has_next': page_obj.has_next(),
                         'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
                         'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
                         })


def getDocuents(request):
    documents = Document.objects.all()
    paginator = Paginator(documents, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    documents_list = [{'id': document.id, 'title': document.title, 'size': document.size, 'resumen': document.resumen,
                       'date': document.date} for document in page_obj]

    return JsonResponse({'documents': documents_list,
                         'has_previous': page_obj.has_previous(),
                         'has_next': page_obj.has_next(),
                         'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
                         'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
                         })


def home(request):
    # authors_list = getAuthors(request)
    return render(request, "repo_App/home/home.html", )


def documents(request):
    documents_list = Document.objects.all()
    if request.method == 'GET':
        return render(request, "repo_App/documents/documents.html", {'documents': documents_list})

    if request.method == 'POST':
        document = Document
        title = request.GET.get('title')
        description = request.GET.get('description')
        size = request.GET.get('size')
        resumen = request.GET.get('resumen')
        file = request.GET.get('file')
        date = request.GET.get('date')

        document(title=title, description=description, size=size, resumen=resumen, file=file, date=date)
        document.save
        return render(request, "repo_App/documents/documents.html", {'documents': documents_list})






def videos(request):
    return render(request, "repo_App/videos/videos.html")


def audios(request):
    return render(request, "repo_App/audios/audios.html")


def images(request):
    return render(request, "repo_App/images/images.html")
