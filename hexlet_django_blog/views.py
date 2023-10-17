from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return redirect(
            reverse('article', kwargs={'tags': 'python', 'article_id': 42})
        )


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags},
    )
