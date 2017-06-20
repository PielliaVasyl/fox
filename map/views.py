from django.shortcuts import render, get_object_or_404

from algoritms.get_filtered_instances import get_filtered_instances
from directions.all.forms import PlacesFilterForm, SchoolsFilterForm, ShopsFilterForm, CustomerServicesFilterForm, \
    HallsFilterForm
from entities.models.pages import Place, School, Shop, CustomerServices, Hall


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

    instances = get_filtered_instances(instances, filters)

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
        'instance': current_place,
        'form': form
    }
    return render(request, 'map/place-single.html', context)


def schools(request, city_title=None, direction_title=None):
    form = SchoolsFilterForm(request.POST or None, direction=direction_title)

    if city_title:
        instances = School.objects.filter(cities__title=city_title)
    else:
        instances = School.objects.all()

    filters = None
    if form.is_valid():
        filters = {}
        for field in form.fields:
            if form.cleaned_data.get(field):
                filters[field] = form.cleaned_data.get(field)

        if not any([value for key, value in filters.items()]):
            filters = None

    instances = get_filtered_instances(instances, filters)

    context = {
        'instances': instances,
        'form': form,
    }
    return render(request, 'map/schools.html', context)


def school(request, school_id, direction_title=None, city_title=None):
    current_school = get_object_or_404(School, pk=school_id)
    title = '%s' % (current_school.title,)

    form = SchoolsFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_school,
        'form': form
    }
    return render(request, 'map/school-single.html', context)


def shops(request, city_title=None, direction_title=None):
    form = ShopsFilterForm(request.POST or None, direction=direction_title)

    if city_title:
        instances = Shop.objects.filter(cities__title=city_title)
    else:
        instances = Shop.objects.all()

    filters = None
    if form.is_valid():
        filters = {}
        for field in form.fields:
            if form.cleaned_data.get(field):
                filters[field] = form.cleaned_data.get(field)

        if not any([value for key, value in filters.items()]):
            filters = None

    instances = get_filtered_instances(instances, filters)

    context = {
        'instances': instances,
        'form': form,
    }
    return render(request, 'map/shops.html', context)


def shop(request, shop_id, direction_title=None, city_title=None):
    current_shop = get_object_or_404(Shop, pk=shop_id)
    title = '%s' % (current_shop.title,)

    form = SchoolsFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_shop,
        'form': form
    }
    return render(request, 'map/shop-single.html', context)


def services(request, city_title=None, direction_title=None):
    form = CustomerServicesFilterForm(request.POST or None, direction=direction_title)

    if city_title:
        instances = CustomerServices.objects.filter(cities__title=city_title)
    else:
        instances = CustomerServices.objects.all()

    filters = None
    if form.is_valid():
        filters = {}
        for field in form.fields:
            if form.cleaned_data.get(field):
                filters[field] = form.cleaned_data.get(field)

        if not any([value for key, value in filters.items()]):
            filters = None

    instances = get_filtered_instances(instances, filters)

    context = {
        'instances': instances,
        'form': form,
    }
    return render(request, 'map/services.html', context)


def service(request, service_id, direction_title=None, city_title=None):
    current_services = get_object_or_404(CustomerServices, pk=service_id)
    title = '%s' % (current_services.title,)

    form = CustomerServicesFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_services,
        'form': form
    }
    return render(request, 'map/service-single.html', context)


def halls(request, city_title=None, direction_title=None):
    form = HallsFilterForm(request.POST or None, direction=direction_title)

    if city_title:
        instances = Hall.objects.filter(cities__title=city_title)
    else:
        instances = Hall.objects.all()

    filters = None
    if form.is_valid():
        filters = {}
        for field in form.fields:
            if form.cleaned_data.get(field):
                filters[field] = form.cleaned_data.get(field)

        if not any([value for key, value in filters.items()]):
            filters = None

    instances = get_filtered_instances(instances, filters)

    context = {
        'instances': instances,
        'form': form,
    }
    return render(request, 'map/halls.html', context)


def hall(request, hall_id, direction_title=None, city_title=None):
    current_hall = get_object_or_404(Hall, pk=hall_id)
    title = '%s' % (current_hall.title,)

    form = HallsFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_hall,
        'form': form
    }
    return render(request, 'map/hall-single.html', context)
