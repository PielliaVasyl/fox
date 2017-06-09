from django.shortcuts import render

from algoritms.entity_schedule import entity_schedule
from directions.dance.forms import EventsFilterForm
from entities.models import Event


def upcoming(request, city_title=None, direction_title=None):
    title = 'Мероприятия'

    filters = None
    current_form = {
        # 'dance': DanceEventsFilterForm,
    }.get(direction_title, EventsFilterForm)

    form = current_form(request.POST or None)
    if form.is_valid():
        filters = {}
        for field in form.fields:
            filters[field] = form.cleaned_data.get(field)

        if not any([value for key, value in filters.items()]):
            filters = None

    events_months = entity_schedule(Event, direction=direction_title, filters=filters)

    context = {
        'title': title,
        'events_months': events_months,
        'form': form,
    }
    return render(request, 'events/events.html', context)
