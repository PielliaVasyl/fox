from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from algoritms.entity_schedule import entity_schedule
from algoritms.get_direction_city_parameter import get_direction_city_parameter
from directions.all.forms import EventsFilterForm, PromoActionFilterForm
from entities.models import DayOfTheWeek
from entities.models import EventType
from entities.models import ExperienceLevel
from entities.models import PriceType
from entities.models import RepeatsType
from entities.models.events import Event, PromoAction
from events.forms import EditEventTitleForm, EditEventDirectionsForm, EditEventCitiesForm, EditEventDescriptionForm, \
    EditEventNoteForm, EditEventImageForm, EditEventVideoForm, EditEventDatesForm, EditEventStatusForm, \
    EditEventTypesForm, EditEventLinksForm, EditEventPriceTypesForm, EditEventExperienceLevelsForm, \
    EditEventRepeatsTypeForm, EditEventScheduleForm, EditEventPolicyForm, EditEventEventLocationForm, \
    EditEventEventDanceClassesForm, EditPromoActionTitleForm, EditPromoActionDirectionsForm, EditPromoActionCitiesForm, \
    EditPromoActionDescriptionForm, EditPromoActionNoteForm, EditPromoActionImageForm, EditPromoActionVideoForm, \
    EditPromoActionDatesForm, EditPromoActionStatusForm, EditPromoActionEventDanceClassesForm, EditPromoActionLinksForm, \
    EditPromoActionPolicyForm


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


def promo_action(request, promo_action_id, direction_title=None, city_title=None):
    current_promo_action = get_object_or_404(PromoAction, pk=promo_action_id)
    title = '%s' % (current_promo_action.title,)

    form = PromoActionFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_promo_action,
        'form': form
    }
    return render(request, 'events/promo-action-single.html', context)


def edit_event(request, event_id, city_title=None, direction_title=None):
    current_event = get_object_or_404(Event, pk=event_id)
    title = '%s' % (current_event.title,)

    context = {
        'title': title,
        'event': current_event,
    }
    return render(request, 'events/event/event-edit.html', context)


def edit_promo_action(request, promo_action_id, city_title=None, direction_title=None):
    current_promo_action = get_object_or_404(PromoAction, pk=promo_action_id)
    title = '%s' % (current_promo_action.title,)

    context = {
        'title': title,
        'promo_action': current_promo_action,
    }
    return render(request, 'events/promo_action/promo-action-edit.html', context)


def edit_event_attr(request, event_id, attribute=None, city_title=None, direction_title=None):
    current_event = get_object_or_404(Event, pk=event_id)
    title = '%s' % (current_event.title,)

    attr = attribute
    html_template_path = 'events/event/edit/edit-' + attribute + '.html'

    if attribute == 'title':
        form = EditEventTitleForm(request.POST or None, initial={'title': current_event.title})
    if attribute == 'directions':
        form = EditEventDirectionsForm(request.POST or None, initial={'directions': current_event.directions.all()})
    if attribute == 'cities':
        form = EditEventCitiesForm(request.POST or None, initial={'cities': current_event.cities.all()})
    if attribute == 'description':
        form = EditEventDescriptionForm(request.POST or None, initial={'description': current_event.description})
    if attribute == 'note':
        form = EditEventNoteForm(request.POST or None, initial={'note': current_event.note})
    if attribute == 'image':
        if request.method == 'POST':
            form = EditEventImageForm(request.POST, request.FILES)
        else:
            form = EditEventImageForm(None, initial={'image': current_event.image})
    if attribute == 'video':
        form = EditEventVideoForm(request.POST or None, initial={'video': current_event.video})
    if attribute == 'dates':
        form = EditEventDatesForm(request.POST or None, initial={'start_date': current_event.start_date,
                                                                 'end_date': current_event.end_date})
        attr = 'end_date'
    if attribute == 'status':
        form = EditEventStatusForm(request.POST or None, initial={'_status': current_event._status})
        attr = '_status'
    if attribute == 'event-locations':
        form = EditEventEventLocationForm(request.POST or None, initial={'locations': current_event.locations.all()})
        attr = 'locations'
    if attribute == 'event-dance-classes':
        form = EditEventEventDanceClassesForm(request.POST or None,
                                              initial={'dance_directions':
                                                       current_event.local_classes.dance_directions.all(),
                                                       'dance_styles': current_event.local_classes.dance_styles.all()})
    if attribute == 'types':
        form = EditEventTypesForm(request.POST or None, initial={'types': current_event.types.all()})
    if attribute == 'event-links':
        form = EditEventLinksForm(request.POST or None, initial={'links': current_event.links.all()})
        attr = 'links'
    if attribute == 'price-types':
        form = EditEventPriceTypesForm(request.POST or None, initial={'price_types': current_event.price_types.all()})
        attr = 'price_types'
    if attribute == 'experience-levels':
        form = EditEventExperienceLevelsForm(request.POST or None,
                                             initial={'experience_levels': current_event.experience_levels.all()})
        attr = 'experience_levels'
    if attribute == 'repeats-type':
        form = EditEventRepeatsTypeForm(request.POST or None, initial={'repeats_type': current_event.repeats_type})
        attr = 'repeats_type'
    if attribute == 'schedule':
        form = EditEventScheduleForm(request.POST or None, initial={'schedule': current_event.schedule.all()})
    if attribute == 'policy':
        form = EditEventPolicyForm(request.POST or None, initial={'owners': current_event.owners.all(),
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
        elif attribute == 'event-dance-classes':
            dance_styles = form.cleaned_data.get('dance_styles')
            setattr(current_event.local_classes, 'dance_styles', dance_styles)
            dance_directions = form.cleaned_data.get('dance_directions')
            setattr(current_event.local_classes, 'dance_directions', dance_directions)
            new_attr = None
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


def edit_promo_action_attr(request, promo_action_id, attribute=None, city_title=None, direction_title=None):
    current_instance = get_object_or_404(PromoAction, pk=promo_action_id)
    title = '%s' % (current_instance.title,)

    attr = attribute
    html_template_path = 'events/promo_action/edit/edit-' + attribute + '.html'

    if attribute == 'title':
        form = EditPromoActionTitleForm(request.POST or None, initial={'title': current_instance.title})
    if attribute == 'directions':
        form = EditPromoActionDirectionsForm(request.POST or None, initial={'directions': current_instance.directions.all()})
    if attribute == 'cities':
        form = EditPromoActionCitiesForm(request.POST or None, initial={'cities': current_instance.cities.all()})
    if attribute == 'description':
        form = EditPromoActionDescriptionForm(request.POST or None, initial={'description': current_instance.description})
    if attribute == 'note':
        form = EditPromoActionNoteForm(request.POST or None, initial={'note': current_instance.note})
    if attribute == 'image':
        if request.method == 'POST':
            form = EditPromoActionImageForm(request.POST, request.FILES)
        else:
            form = EditPromoActionImageForm(None, initial={'image': current_instance.image})
    if attribute == 'video':
        form = EditPromoActionVideoForm(request.POST or None, initial={'video': current_instance.video})
    if attribute == 'dates':
        form = EditPromoActionDatesForm(request.POST or None, initial={'start_date': current_instance.start_date,
                                                                 'end_date': current_instance.end_date})
        attr = 'end_date'
    if attribute == 'status':
        form = EditPromoActionStatusForm(request.POST or None, initial={'_status': current_instance._status})
        attr = '_status'
    if attribute == 'event-dance-classes':
        form = EditPromoActionEventDanceClassesForm(request.POST or None,
                                              initial={'dance_directions':
                                                        current_instance.local_classes.dance_directions.all(),
                                                       'dance_styles': current_instance.local_classes.dance_styles.all()})
    if attribute == 'promo-action-links':
        form = EditPromoActionLinksForm(request.POST or None, initial={'links': current_instance.links.all()})
        attr = 'links'
    if attribute == 'policy':
        form = EditPromoActionPolicyForm(request.POST or None, initial={'owners': current_instance.owners.all(),
                                                                  'contributors': current_instance.contributors.all(),
                                                                  'author': current_instance.author})
        attr = 'author'

    if form.is_valid():
        if attribute == 'image':
            if 'image' in request.FILES:
                new_attr = request.FILES['image']
            else:
                new_attr = None
        elif attribute == 'dates':
            start_date = form.cleaned_data.get('start_date')
            setattr(current_instance, 'start_date', start_date)
            new_attr = form.cleaned_data.get(attr)
        elif attribute == 'event-dance-classes':
            dance_styles = form.cleaned_data.get('dance_styles')
            setattr(current_instance.local_classes, 'dance_styles', dance_styles)
            dance_directions = form.cleaned_data.get('dance_directions')
            setattr(current_instance.local_classes, 'dance_directions', dance_directions)
            new_attr = None
        elif attribute == 'policy':
            owners = form.cleaned_data.get('owners')
            setattr(current_instance, 'owners', owners)
            contributors = form.cleaned_data.get('contributors')
            setattr(current_instance, 'contributors', contributors)
            new_attr = form.cleaned_data.get(attr)
        else:
            new_attr = form.cleaned_data.get(attr)
        setattr(current_instance, attr, new_attr)
        current_instance.save()
        return HttpResponseRedirect('/events/promo-action-%s/edit/%s' %
                                    (current_instance.pk, get_direction_city_parameter(city_title, direction_title)))

    context = {
        'title': title,
        'instance': current_instance,
        'form': form
    }
    return render(request, html_template_path, context)
