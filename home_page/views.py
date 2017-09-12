from django.http import HttpResponseRedirect
from django.shortcuts import render

from algoritms.Util import get_is_direction_city_changed


def index(request, city_title=None, direction_title=None):
    title = 'Сообщество активных людей'
    direction_city_changed, context = get_is_direction_city_changed(request, city_title, direction_title)

    if direction_city_changed:
        return HttpResponseRedirect('/' + direction_city_changed)

    context['title'] = title

    return render(request, 'base.html', context)
