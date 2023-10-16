from django.shortcuts import render
from django.views import View


class IndexView(View):

    def get(self, request):
        return render(
            request,
            'articles/index.html',
            context={'name': 'hexlet_django_blog'}
        )
