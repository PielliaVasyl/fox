from django.shortcuts import render, get_object_or_404

from algoritms.entity_schedule import entity_schedule
from directions.dance.forms import EventsFilterForm
from entities.models.events import Event


def _get_local_class_title(direction_title):
    return {
        'dance': '<h3>Стили</h3><small>танцев</small>'
    }.get(direction_title, '<h3>Направление</h3><small>мероприятия</small>')


def upcoming(request, city_title=None, direction_title=None):
    title = 'Мероприятия'

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
    context = {
        'title': title,
        'events_months': events_months,
        'form': form,
        'local_class_title': local_class_title
    }
    return render(request, 'events/events.html', context)


def past(request, city_title=None, direction_title=None):
    title = 'Мероприятия'

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
    context = {
        'title': title,
        'events_months': events_months,
        'form': form,
        'local_class_title': local_class_title
    }
    return render(request, 'events/events.html', context)


def event(request, event_id, direction_title=None, city_title=None):
    current_event = get_object_or_404(Event, pk=event_id)
    title = '%s' % (current_event.title,)

    form = EventsFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'event': current_event,
        'form': form
    }
    return render(request, 'events/event-single.html', context)
