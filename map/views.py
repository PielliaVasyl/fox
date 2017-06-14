from django.shortcuts import render, get_object_or_404

from algoritms.entity_schedule import _get_filtered_instances
from directions.all.forms import PlacesFilterForm
from entities.models.pages import Place


def places(request, city_title=None, direction_title=None):

    form = PlacesFilterForm(request.POST or None, direction=direction_title)

    if city_title:
        instances = Place.objects.filter(cities__title=city_title)
    else:
        instances = Place.objects.all()

    filters = None
    if form.is_valid():
        filters = {}
        for field in form.fields:
            if form.cleaned_data.get(field):
                filters[field] = form.cleaned_data.get(field)

        if not any([value for key, value in filters.items()]):
            filters = None

    instances = _get_filtered_instances(instances, filters)

    context = {
        'instances': instances,
        'form': form,
    }
    return render(request, 'map/places.html', context)


def place(request, place_id, direction_title=None, city_title=None):
    current_place = get_object_or_404(Place, pk=place_id)
    title = '%s' % (current_place.title,)

    form = PlacesFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'place': current_place,
        'form': form
    }
    return render(request, 'map/place-single.html', context)
