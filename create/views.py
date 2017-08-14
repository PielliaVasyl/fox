from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from algoritms.get_direction_city_parameter import get_direction_city_parameter
from entities.forms import EventLocationForm
from entities.forms import PlaceLocationForm
from entities.forms.classes import DirectionForm, CityForm
from entities.forms.events import CutEventForm, CutPromoActionForm, CutPlaceForm
from entities.forms.links import EventLinkForm, PromoActionLinkForm, PlaceLinkForm
from entities.forms.locations import CutPlaceLocationForm, PlaceMapCoordinatesForm


def create(request, city_title=None, direction_title=None):
    context = {
    }
    return render(request, 'create/create.html', context)


def create_event(request, city_title=None, direction_title=None):
    form = CutEventForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponseRedirect('/events/event-%s/edit/%s' %
                                    (instance.pk, get_direction_city_parameter(city_title, direction_title)))
    context = {
        'form': form,

    }
    return render(request, 'create/create-event.html', context)


def create_promo_action(request, city_title=None, direction_title=None):
    form = CutPromoActionForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponseRedirect('/events/promo-action-%s/edit/%s' %
                                    (instance.pk, get_direction_city_parameter(city_title, direction_title)))
    context = {
        'form': form,

    }
    return render(request, 'create/create-promo-action.html', context)


def create_place(request, city_title=None, direction_title=None):
    form = CutPlaceForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponseRedirect('/map/place-%s/edit/%s' %
                                    (instance.pk, get_direction_city_parameter(city_title, direction_title)))
    context = {
        'form': form,
    }
    return render(request, 'create/create-place.html', context)


def create_attr(request, attribute=None, city_title=None, direction_title=None):
    html_template_path = 'create/create-attr-' + attribute + '.html'
    if attribute == 'direction':
        form = DirectionForm(request.POST or None)
    if attribute == 'city':
        form = CityForm(request.POST or None)
    if attribute == 'event-link':
        form = EventLinkForm(request.POST or None)
    if attribute == 'place-link':
        form = PlaceLinkForm(request.POST or None)
    if attribute == 'promo-action-link':
        form = PromoActionLinkForm(request.POST or None)
    if attribute == 'event-location':
        form = EventLocationForm(request.POST or None)
    if attribute == 'place-location':
        form = CutPlaceLocationForm(request.POST or None)
        form1 = PlaceMapCoordinatesForm(request.POST or None)
        if form.is_valid():
            coordinates = form1.save()
            location = form.save(commit=False)
            location.coordinates = coordinates
            location.save()
            return HttpResponseRedirect('/%s/%s/edit/%s' %
                                        (get_section(request.GET.get('instance')),
                                         request.GET.get('instance'),
                                         get_direction_city_parameter(city_title, direction_title)
                                         ))
        context = {
            'form': form,
            'form1': form1,
            'incoming_instance': request.GET.get('instance')

        }
        return render(request, html_template_path, context)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/%s/%s/edit/%s' %
                                    (get_section(request.GET.get('instance')),
                                     request.GET.get('instance'),
                                     get_direction_city_parameter(city_title, direction_title)
                                     ))
    context = {
        'form': form,
        'incoming_instance': request.GET.get('instance')

    }
    return render(request, html_template_path, context)


def get_section(instance):
    if 'event-' in instance or 'promo-action-' in instance:
        return 'events'
    if 'place-' in instance:
        return 'map'
    return ''
