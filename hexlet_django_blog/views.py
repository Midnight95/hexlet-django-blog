from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return redirect(
            reverse('about')
        )


def about(request):
    tags = ['обучение', 'программирование', 'python', 'oop']
    return render(
        request,
        'about.html',
        context={'tags': tags},
    )
