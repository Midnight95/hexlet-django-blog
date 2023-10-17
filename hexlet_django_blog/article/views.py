from django.shortcuts import render
from django.views import View

from hexlet_django_blog.article.models import Article


class IndexView(View):

    def get(self, request):
        articles = Article.objects.all()[:15]
        return render(
            request,
            'articles/index.html',
            context={
                'name': 'hexlet_django_blog',
                'articles': articles,
                }
        )


def index(request, tags: str = None, article_id: int = None):
    return render(request, 'articles/index.html', context={
        'article_id': article_id,
        'tags': tags,
        'name': 'article'
    })
