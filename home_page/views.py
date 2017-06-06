from django.shortcuts import render


def index(request):
    title = 'Сообщество активных людей'
    context = {
        'title': title,
    }
    return render(request, 'base.html', context)
