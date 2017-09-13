from django.http import HttpResponseRedirect
from django.shortcuts import render

from algoritms.Util import get_is_direction_city_changed
from algoritms.entity_schedule import entity_schedule
from directions.all.forms import EventsFilterForm

from entities.models.events import Event


def _get_local_class_title(direction_title):
    return {
        'dance': '<h3>Стили</h3><small>танцев</small>'
    }.get(direction_title, '<h3>Направление</h3><small>мероприятия</small>')


def upcoming(request, city_title=None, direction_title=None):
    title = 'Мероприятия'

    direction_city_changed, context = get_is_direction_city_changed(request, city_title, direction_title)
    if direction_city_changed:
        return HttpResponseRedirect('/events/upcoming/' + direction_city_changed)

    filters = None

    form = EventsFilterForm(request.POST or None, direction=direction_title)
    if form.is_valid():
        filters = {}
        for field in form.fields:
            if form.cleaned_data.get(field):
                filters[field] = form.cleaned_data.get(field)

        if not any([value for key, value in filters.items()]):
            filters = None

    events_months = entity_schedule(Event, direction=direction_title, filters=filters)
    local_class_title = _get_local_class_title(direction_title)

    context['title'] = title
    context['events_months'] = events_months
    context['form'] = form
    context['local_class_title'] = local_class_title

    return render(request, 'events/events.html', context)


def past(request, city_title=None, direction_title=None):
    title = 'Мероприятия'

    direction_city_changed, context = get_is_direction_city_changed(request, city_title, direction_title)
    if direction_city_changed:
        return HttpResponseRedirect('/events/past/' + direction_city_changed)

    filters = None

    form = EventsFilterForm(request.POST or None, direction=direction_title)
    if form.is_valid():
        filters = {}
        for field in form.fields:
            if form.cleaned_data.get(field):
                filters[field] = form.cleaned_data.get(field)

        if not any([value for key, value in filters.items()]):
            filters = None

    events_months = entity_schedule(Event, direction=direction_title, filters=filters, archive=True)
    local_class_title = _get_local_class_title(direction_title)

    context['title'] = title
    context['events_months'] = events_months
    context['form'] = form
    context['local_class_title'] = local_class_title

    return render(request, 'events/events.html', context)
