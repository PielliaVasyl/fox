from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from algoritms.entity_schedule import entity_schedule
from algoritms.get_direction_city_parameter import get_direction_city_parameter
from directions.all.forms import EventsFilterForm
from entities.models import DayOfTheWeek
from entities.models import EventType
from entities.models import ExperienceLevel
from entities.models import PriceType
from entities.models import RepeatsType
from entities.models.events import Event
from events.forms import EditTitleForm, EditDirectionsForm, EditCitiesForm, EditDescriptionForm, EditNoteForm, \
    EditImageForm, EditVideoForm, EditDatesForm, EditStatusForm, EditTypesForm, EditLinksForm, EditPriceTypesForm, \
    EditExperienceLevelsForm, EditRepeatsTypeForm, EditScheduleForm, EditPolicyForm, EditEventLocationForm
from fox_knows.settings import MEDIA_ROOT


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


def edit_attr(request, event_id, attribute=None, city_title=None, direction_title=None):
    current_event = get_object_or_404(Event, pk=event_id)
    title = '%s' % (current_event.title,)

    attr = attribute
    html_template_path = 'events/edit-' + attribute + '.html'

    if attribute == 'title':
        form = EditTitleForm(request.POST or None, initial={'title': current_event.title})
    if attribute == 'directions':
        form = EditDirectionsForm(request.POST or None, initial={'directions': current_event.directions.all()})
    if attribute == 'cities':
        form = EditCitiesForm(request.POST or None, initial={'cities': current_event.cities.all()})
    if attribute == 'description':
        form = EditDescriptionForm(request.POST or None, initial={'description': current_event.description})
    if attribute == 'note':
        form = EditNoteForm(request.POST or None, initial={'note': current_event.note})
    if attribute == 'image':
        if request.method == 'POST':
            form = EditImageForm(request.POST, request.FILES)
        else:
            form = EditImageForm(None, initial={'image': current_event.image})
    if attribute == 'video':
        form = EditVideoForm(request.POST or None, initial={'video': current_event.video})
    if attribute == 'dates':
        form = EditDatesForm(request.POST or None, initial={'start_date': current_event.start_date,
                                                            'end_date': current_event.end_date})
        attr = 'end_date'
    if attribute == 'status':
        form = EditStatusForm(request.POST or None, initial={'status': current_event.status})
        attr = '_status'
    if attribute == 'event-locations':
        form = EditEventLocationForm(request.POST or None, initial={'locations': current_event.locations.all()})
        attr = 'locations'
    if attribute == 'types':
        form = EditTypesForm(request.POST or None, initial={'types': current_event.types.all()})
    if attribute == 'event-links':
        form = EditLinksForm(request.POST or None, initial={'links': current_event.links.all()})
        attr = 'links'
    if attribute == 'price-types':
        form = EditPriceTypesForm(request.POST or None, initial={'price_types': current_event.price_types.all()})
        attr = 'price_types'
    if attribute == 'experience-levels':
        form = EditExperienceLevelsForm(request.POST or None,
                                        initial={'experience_levels': current_event.experience_levels.all()})
        attr = 'experience_levels'
    if attribute == 'repeats-type':
        form = EditRepeatsTypeForm(request.POST or None, initial={'repeats_type': current_event.repeats_type})
        attr = 'repeats_type'
    if attribute == 'schedule':
        form = EditScheduleForm(request.POST or None, initial={'schedule': current_event.schedule.all()})
    if attribute == 'policy':
        form = EditPolicyForm(request.POST or None, initial={'owners': current_event.owners.all(),
                                                             'contributors': current_event.contributors.all(),
                                                             'author': current_event.author})
        attr = 'author'

    if form.is_valid():
        if attribute == 'image':
            if 'image' in request.FILES:
                new_attr = request.FILES['image']
            else:
                new_attr = None
        elif attribute == 'dates':
            start_date = form.cleaned_data.get('start_date')
            setattr(current_event, 'start_date', start_date)
            new_attr = form.cleaned_data.get(attr)
        elif attribute == 'types':
            new_attr = EventType.objects.filter(title__in=form.cleaned_data.get(attr))
        elif attribute == 'price-types':
            new_attr = PriceType.objects.filter(title__in=form.cleaned_data.get(attr))
        elif attribute == 'experience-levels':
            new_attr = ExperienceLevel.objects.filter(title__in=form.cleaned_data.get(attr))
        elif attribute == 'repeats-type':
            new_attr = RepeatsType.objects.filter(title=form.cleaned_data.get(attr))
            if new_attr:
                new_attr = new_attr[0]
            else:
                new_attr = None
        elif attribute == 'schedule':
            new_attr = DayOfTheWeek.objects.filter(title__in=form.cleaned_data.get(attr))
        elif attribute == 'policy':
            owners = form.cleaned_data.get('owners')
            setattr(current_event, 'owners', owners)
            contributors = form.cleaned_data.get('contributors')
            setattr(current_event, 'contributors', contributors)
            new_attr = form.cleaned_data.get(attr)
        else:
            new_attr = form.cleaned_data.get(attr)
        setattr(current_event, attr, new_attr)
        current_event.save()
        return HttpResponseRedirect('/events/event-%s/edit/%s' %
                                    (current_event.pk, get_direction_city_parameter(city_title, direction_title)))

    context = {
        'title': title,
        'event': current_event,
        'form': form
    }
    return render(request, html_template_path, context)

