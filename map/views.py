from django.shortcuts import render

from entities.models.pages import Place


def places(request, city_title=None, direction_title=None):

    form = PlacesFilterForm(request.POST or None)

    if city_title:
        instances = Place.objects.filter(cities__title=city_title)
    else:
        instances = Place.objects.all()

    filters = None
    # if form.is_valid():
    #     place_types = form.cleaned_data.get('place_types')
    #     dance_styles = form.cleaned_data.get('dance_styles')
    #     if place_types or dance_styles:
    #         filters = {}
    #         if place_types:
    #             filters['place_types'] = place_types
    #         if dance_styles:
    #             filters['dance_styles'] = dance_styles

    # instances = _get_filtered_instances(instances, filters)

    context = {
        'instances': instances,
        # 'form': form,
    }
    return render(request, 'map/places.html', context)
