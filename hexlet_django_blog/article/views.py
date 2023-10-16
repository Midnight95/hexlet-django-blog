from django.shortcuts import render


def index(request):
    return render(
        request,
        'articles/index.html',
        context={'name': 'hexlet_django_blog'}
    )
