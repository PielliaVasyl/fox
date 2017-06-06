from django.shortcuts import render


def index(request, city_title=None, direction_title=None):
    title = 'Сообщество активных людей'
    context = {
        'title': title,
        'city_title': city_title,
        'direction_title': direction_title
    }
    return render(request, 'base.html', context)
