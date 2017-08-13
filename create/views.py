from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from algoritms.get_direction_city_parameter import get_direction_city_parameter
from entities.forms import EventLocationForm
from entities.forms.classes import DirectionForm, CityForm
from entities.forms.events import CutEventForm, CutPromoActionForm
from entities.forms.links import EventLinkForm, PromoActionLinkForm


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


def create_attr(request, attribute=None, city_title=None, direction_title=None):
    html_template_path = 'create/create-attr-' + attribute + '.html'
    if attribute == 'direction':
        form = DirectionForm(request.POST or None)
    if attribute == 'city':
        form = CityForm(request.POST or None)
    if attribute == 'event-link':
        form = EventLinkForm(request.POST or None)
    if attribute == 'promo-action-link':
        form = PromoActionLinkForm(request.POST or None)
    if attribute == 'event-location':
        form = EventLocationForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/events/%s/edit/%s' %
                                    (request.GET.get('instance'),
                                     get_direction_city_parameter(city_title, direction_title)
                                     ))
    context = {
        'form': form,
        'incoming_instance': request.GET.get('instance')

    }
    return render(request, html_template_path, context)
