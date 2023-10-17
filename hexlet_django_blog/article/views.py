from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(
            request,
            'articles/index.html',
            context={'name': 'hexlet_django_blog'}
        )


def index(request, tags: str = None, article_id: int = None):
    return render(request, 'articles/index.html', context={
        'article_id': article_id,
        'tags': tags,
        'name': 'article'
    })
