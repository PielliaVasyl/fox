from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from algoritms.get_direction_city_parameter import get_direction_city_parameter
from entities.forms.classes import DirectionForm
from entities.forms.events import CutEventForm
from entities.models.classes import Direction
from entities.models.events import Event


def create(request, city_title=None, direction_title=None):
    # user_profile = get_object_or_404(UserProfile, pk=profile_id)
    # title = '%s' % (user_profile.user.username,)
    context = {
        # 'title': title,
        # 'instance': user_profile,
    }
    return render(request, 'create/create.html', context)


def create_event(request, city_title=None, direction_title=None):
    form = CutEventForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponseRedirect('/events/event-%s/%s' %
                                    (instance.pk, get_direction_city_parameter(city_title, direction_title)))
    context = {
        'form': form,

    }
    return render(request, 'create/create-event.html', context)


def create_attr_direction(request, city_title=None, direction_title=None):
    form = DirectionForm(request.POST or None)
    if form.is_valid():
        instance = form.save()
        return HttpResponseRedirect('/events/%s/edit/%s' %
                                    (request.GET.get('instance'),
                                     get_direction_city_parameter(city_title, direction_title)
                                     ))
    context = {
        'form': form,
        'incoming_instance': request.GET.get('instance')

    }
    return render(request, 'create/create-attr-direction.html', context)
