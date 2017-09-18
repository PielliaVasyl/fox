from django.http import HttpResponseRedirect
from django.shortcuts import render

from algoritms.Util import get_is_direction_city_changed, get_session_direction_city_id


def index(request, city_title=None, direction_title=None):
    title = 'Сообщество активных людей'
    request.session['direction_id'], request.session['city_id'] = \
        get_session_direction_city_id(direction_title, city_title)
    direction_city_changed, context = get_is_direction_city_changed(request, city_title, direction_title)

    if direction_city_changed:
        return HttpResponseRedirect('/' + direction_city_changed)

    context['title'] = title

    return render(request, 'base.html', context)
