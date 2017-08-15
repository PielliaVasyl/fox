from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from algoritms.get_direction_city_parameter import get_direction_city_parameter
from algoritms.get_filtered_instances import get_filtered_instances
from directions.all.forms import PlacesFilterForm, SchoolsFilterForm, ShopsFilterForm, CustomerServicesFilterForm, \
    HallsFilterForm
from entities.models import PlaceType
from entities.models import SchoolContacts
from entities.models.pages import Place, School, Shop, CustomerServices, Hall
from map.forms import EditPlaceDirectionsForm, EditPlaceDescriptionForm, EditPlaceImageForm, EditPlaceTypesForm, \
    EditPlaceLinksForm, EditPlacePlaceDanceClassesForm, EditPlacePolicyForm, EditPlacePlaceLocationForm, \
    EditSchoolTitleForm, EditSchoolDirectionsForm, EditSchoolSchoolDanceClassesForm, EditSchoolCitiesForm, \
    EditSchoolDescriptionForm, EditSchoolImageForm, EditSchoolSchoolLocationForm, EditSchoolLinksForm, \
    EditSchoolPolicyForm, EditSchoolEmployeesForm, EditSchoolSchoolContactForm, EditSchoolSocialsForm
from map.forms import EditPlaceTitleForm, EditPlaceCitiesForm


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
    return render(request, 'map/place/places.html', context)


def place(request, instance_id, direction_title=None, city_title=None):
    current_place = get_object_or_404(Place, pk=instance_id)
    title = '%s' % (current_place.title,)

    form = PlacesFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_place,
        'form': form
    }
    return render(request, 'map/place/place-single.html', context)


def edit_place(request, instance_id, city_title=None, direction_title=None):
    instance = get_object_or_404(Place, pk=instance_id)
    title = '%s' % (instance.title,)

    context = {
        'title': title,
        'instance': instance,
    }
    return render(request, 'map/place/place-edit.html', context)


def edit_place_attr(request, instance_id, attribute=None, city_title=None, direction_title=None):
    instance = get_object_or_404(Place, pk=instance_id)
    title = '%s' % (instance.title,)

    attr = attribute
    html_template_path = 'map/place/edit/edit-' + attribute + '.html'

    if attribute == 'title':
        form = EditPlaceTitleForm(request.POST or None, initial={'title': instance.title})
    if attribute == 'directions':
        form = EditPlaceDirectionsForm(request.POST or None, initial={'directions': instance.directions.all()})
    if attribute == 'cities':
        form = EditPlaceCitiesForm(request.POST or None, initial={'cities': instance.cities.all()})
    if attribute == 'description':
        form = EditPlaceDescriptionForm(request.POST or None, initial={'description': instance.description})
    if attribute == 'image':
        if request.method == 'POST':
            form = EditPlaceImageForm(request.POST, request.FILES)
        else:
            form = EditPlaceImageForm(None, initial={'image': instance.image})
    if attribute == 'place-locations':
        form = EditPlacePlaceLocationForm(request.POST or None, initial={'locations': instance.locations.all()})
        attr = 'locations'
    if attribute == 'place-dance-classes':
        form = EditPlacePlaceDanceClassesForm(request.POST or None,
                                              initial={'dance_directions':
                                                        instance.local_classes.dance_directions.all(),
                                                       'dance_styles': instance.local_classes.dance_styles.all()})
    if attribute == 'types':
        form = EditPlaceTypesForm(request.POST or None, initial={'types': instance.types.all()})
    if attribute == 'place-links':
        form = EditPlaceLinksForm(request.POST or None, initial={'links': instance.links.all()})
        attr = 'links'
    if attribute == 'policy':
        form = EditPlacePolicyForm(request.POST or None, initial={'owners': instance.owners.all(),
                                                                  'contributors': instance.contributors.all(),
                                                                  'author': instance.author})
        attr = 'author'

    if form.is_valid():
        if attribute == 'image':
            if 'image' in request.FILES:
                new_attr = request.FILES['image']
            else:
                new_attr = None
        elif attribute == 'place-dance-classes':
            dance_styles = form.cleaned_data.get('dance_styles')
            setattr(instance.local_classes, 'dance_styles', dance_styles)
            dance_directions = form.cleaned_data.get('dance_directions')
            setattr(instance.local_classes, 'dance_directions', dance_directions)
            new_attr = None
        elif attribute == 'types':
            new_attr = PlaceType.objects.filter(title__in=form.cleaned_data.get(attr))
        elif attribute == 'policy':
            owners = form.cleaned_data.get('owners')
            setattr(instance, 'owners', owners)
            contributors = form.cleaned_data.get('contributors')
            setattr(instance, 'contributors', contributors)
            new_attr = form.cleaned_data.get(attr)
        else:
            new_attr = form.cleaned_data.get(attr)
        setattr(instance, attr, new_attr)
        instance.save()
        return HttpResponseRedirect('/map/places/place-%s/edit/%s' %
                                    (instance.pk, get_direction_city_parameter(city_title, direction_title)))

    context = {
        'title': title,
        'instance': instance,
        'form': form
    }
    return render(request, html_template_path, context)


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
    return render(request, 'map/school/schools.html', context)


def school(request, instance_id, direction_title=None, city_title=None):
    current_school = get_object_or_404(School, pk=instance_id)
    title = '%s' % (current_school.title,)

    form = SchoolsFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_school,
        'form': form
    }
    return render(request, 'map/school/school-single.html', context)


def edit_school(request, instance_id, city_title=None, direction_title=None):
    instance = get_object_or_404(School, pk=instance_id)
    title = '%s' % (instance.title,)

    context = {
        'title': title,
        'instance': instance,
    }
    return render(request, 'map/school/school-edit.html', context)


def edit_school_attr(request, instance_id, attribute=None, city_title=None, direction_title=None):
    instance = get_object_or_404(School, pk=instance_id)
    title = '%s' % (instance.title,)

    attr = attribute
    html_template_path = 'map/school/edit/edit-' + attribute + '.html'

    if attribute == 'title':
        form = EditSchoolTitleForm(request.POST or None, initial={'title': instance.title})
    if attribute == 'directions':
        form = EditSchoolDirectionsForm(request.POST or None, initial={'directions': instance.directions.all()})
    if attribute == 'cities':
        form = EditSchoolCitiesForm(request.POST or None, initial={'cities': instance.cities.all()})
    if attribute == 'description':
        form = EditSchoolDescriptionForm(request.POST or None, initial={'description': instance.description})
    if attribute == 'image':
        if request.method == 'POST':
            form = EditSchoolImageForm(request.POST, request.FILES)
        else:
            form = EditSchoolImageForm(None, initial={'image': instance.image})
    if attribute == 'school-locations':
        form = EditSchoolSchoolLocationForm(request.POST or None, initial={'locations': instance.locations.all()})
        attr = 'locations'
    if attribute == 'employees':
        form = EditSchoolEmployeesForm(request.POST or None, initial={'employees': instance.employees.all()})
    if attribute == 'school-dance-classes':
        form = EditSchoolSchoolDanceClassesForm(request.POST or None,
                                                initial={'dance_directions':
                                                         instance.local_classes.dance_directions.all(),
                                                         'dance_styles': instance.local_classes.dance_styles.all()})
    if attribute == 'school-links':
        form = EditSchoolLinksForm(request.POST or None, initial={'links': instance.links.all()})
        attr = 'links'
    if attribute == 'school-contacts':
        form_contact = EditSchoolSchoolContactForm(request.POST or None,
                                                   initial={'phone_numbers': instance.contacts.phone_numbers.all()})
        form_socials = EditSchoolSocialsForm(request.POST or None, initial={'links': instance.links.all()})
        attr = 'contacts'
        if form_contact.is_valid():
            phone_numbers = form_contact.cleaned_data.get('phone_numbers')
            new_attr = SchoolContacts.objects.get(author_id=instance.author_id)
            new_attr.phone_numbers = phone_numbers
            setattr(instance, attr, new_attr)
            instance.save()
        if form_socials.is_valid():
            pass
        if form_contact.is_valid() or form_socials.is_valid():
            return HttpResponseRedirect('/map/schools/school-%s/edit/%s' %
                                        (instance.pk, get_direction_city_parameter(city_title, direction_title)))

        context = {
            'title': title,
            'instance': instance,
            'form_contact': form_contact,
            'form_socials': form_socials
        }
        return render(request, html_template_path, context)
    if attribute == 'policy':
        form = EditSchoolPolicyForm(request.POST or None, initial={'owners': instance.owners.all(),
                                                                   'contributors': instance.contributors.all(),
                                                                   'author': instance.author})
        attr = 'author'

    if form.is_valid():
        if attribute == 'image':
            if 'image' in request.FILES:
                new_attr = request.FILES['image']
            else:
                new_attr = None
        elif attribute == 'school-dance-classes':
            dance_styles = form.cleaned_data.get('dance_styles')
            setattr(instance.local_classes, 'dance_styles', dance_styles)
            dance_directions = form.cleaned_data.get('dance_directions')
            setattr(instance.local_classes, 'dance_directions', dance_directions)
            new_attr = None
        elif attribute == 'policy':
            owners = form.cleaned_data.get('owners')
            setattr(instance, 'owners', owners)
            contributors = form.cleaned_data.get('contributors')
            setattr(instance, 'contributors', contributors)
            new_attr = form.cleaned_data.get(attr)
        else:
            new_attr = form.cleaned_data.get(attr)
        setattr(instance, attr, new_attr)
        instance.save()
        return HttpResponseRedirect('/map/schools/school-%s/edit/%s' %
                                    (instance.pk, get_direction_city_parameter(city_title, direction_title)))

    context = {
        'title': title,
        'instance': instance,
        'form': form
    }
    return render(request, html_template_path, context)


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
    return render(request, 'map/shop/shops.html', context)


def shop(request, shop_id, direction_title=None, city_title=None):
    current_shop = get_object_or_404(Shop, pk=shop_id)
    title = '%s' % (current_shop.title,)

    form = SchoolsFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_shop,
        'form': form
    }
    return render(request, 'map/shop/shop-single.html', context)


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
    return render(request, 'map/service/services.html', context)


def service(request, service_id, direction_title=None, city_title=None):
    current_services = get_object_or_404(CustomerServices, pk=service_id)
    title = '%s' % (current_services.title,)

    form = CustomerServicesFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_services,
        'form': form
    }
    return render(request, 'map/service/service-single.html', context)


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
    return render(request, 'map/hall/halls.html', context)


def hall(request, hall_id, direction_title=None, city_title=None):
    current_hall = get_object_or_404(Hall, pk=hall_id)
    title = '%s' % (current_hall.title,)

    form = HallsFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_hall,
        'form': form
    }
    return render(request, 'map/hall/hall-single.html', context)
