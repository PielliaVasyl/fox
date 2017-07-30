from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from algoritms.entity_schedule import entity_schedule
from algoritms.get_direction_city_parameter import get_direction_city_parameter
from directions.all.forms import EventsFilterForm
from entities.models.events import Event
from events.forms import EditTitleForm, EditDirectionsForm


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


def edit_event(request, event_id, city_title=None, direction_title=None):
    current_event = get_object_or_404(Event, pk=event_id)
    title = '%s' % (current_event.title,)

    context = {
        'title': title,
        'event': current_event,
    }
    return render(request, 'events/event-edit.html', context)


def edit_title(request, event_id, city_title=None, direction_title=None):
    current_event = get_object_or_404(Event, pk=event_id)
    title = '%s' % (current_event.title,)
    edit_title_form = EditTitleForm(request.POST or None, initial={'title': current_event.title})
    if edit_title_form.is_valid():
        new_title = edit_title_form.cleaned_data.get('title')
        current_event.title = new_title
        current_event.save()
        return HttpResponseRedirect('/events/event-%s/edit/%s' %
                                    (current_event.pk, get_direction_city_parameter(city_title, direction_title)))

    context = {
        'title': title,
        'event': current_event,
        'edit_title_form': edit_title_form
    }
    return render(request, 'events/edit-title.html', context)


def edit_directions(request, event_id, city_title=None, direction_title=None):
    current_event = get_object_or_404(Event, pk=event_id)
    title = '%s' % (current_event.title,)
    edit_directions_form = EditDirectionsForm(request.POST or None, initial={'directions': current_event.directions.all()})
    if edit_directions_form.is_valid():
        new_directions = edit_directions_form.cleaned_data.get('directions')
        current_event.directions = new_directions
        current_event.save()
        return HttpResponseRedirect('/events/event-%s/edit/%s' %
                                    (current_event.pk, get_direction_city_parameter(city_title, direction_title)))

    context = {
        'title': title,
        'event': current_event,
        'edit_directions_form': edit_directions_form
    }
    return render(request, 'events/edit-directions.html', context)
