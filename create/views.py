from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from algoritms.get_direction_city_parameter import get_direction_city_parameter
from entities.forms import EventLocationForm
from entities.forms import PhoneNumberForm
from entities.forms.classes import DirectionForm, CityForm
from entities.forms.events import CutEventForm, CutPromoActionForm
from entities.forms.links import EventLinkForm, PromoActionLinkForm, PlaceLinkForm, SchoolLinkForm, TeacherLinkForm, \
    OrganizationLinkForm, PersonLinkForm, ResourceLinkForm
from entities.forms.locations import CutPlaceLocationForm, PlaceMapCoordinatesForm, SchoolMapCoordinatesForm, \
    CutSchoolLocationForm, OrganizationMapCoordinatesForm, CutOrganizationLocationForm
from entities.forms.pages import CutPlaceForm, CutSchoolForm, CutTeacherForm, CutOrganizationForm, CutPersonForm, \
    CutResourceForm


def create(request, city_title=None, direction_title=None):
    context = {
    }
    return render(request, 'create/create.html', context)


def create_instance(request, instance=None, city_title=None, direction_title=None):
    form = {
        'event': CutEventForm(request.POST or None),
        'promo-action': CutPromoActionForm(request.POST or None),
        'place': CutPlaceForm(request.POST or None),
        'school': CutSchoolForm(request.POST or None),
        'teacher': CutTeacherForm(request.POST or None),
        'organization': CutOrganizationForm(request.POST or None),
        'person': CutPersonForm(request.POST or None),
        'resource': CutResourceForm(request.POST or None),

    }.get(instance, None)

    if form.is_valid():
        my_instance = form.save()
        return HttpResponseRedirect('/' + instance + '-%s/edit/%s' %
                                    (my_instance.pk, get_direction_city_parameter(city_title, direction_title)))
    context = {
        'form': form,
    }
    return render(request, 'create/create-' + instance + '.html', context)


def create_attr(request, attribute=None, city_title=None, direction_title=None):
    html_template_path = 'create/attrs/create-attr-' + attribute + '.html'
    if attribute == 'direction':
        form = DirectionForm(request.POST or None)
    if attribute == 'city':
        form = CityForm(request.POST or None)
    if attribute == 'event-link':
        form = EventLinkForm(request.POST or None)
    if attribute == 'place-link':
        form = PlaceLinkForm(request.POST or None)
    if attribute == 'school-link':
        form = SchoolLinkForm(request.POST or None)
    if attribute == 'organization-link':
        form = OrganizationLinkForm(request.POST or None)
    if attribute == 'teacher-link':
        form = TeacherLinkForm(request.POST or None)
    if attribute == 'person-link':
        form = PersonLinkForm(request.POST or None)
    if attribute == 'promo-action-link':
        form = PromoActionLinkForm(request.POST or None)
    if attribute == 'resource-link':
        form = ResourceLinkForm(request.POST or None)
    if attribute == 'event-location':
        form = EventLocationForm(request.POST or None)
    if attribute in ['place-location', 'school-location', 'organization-location']:
        if attribute == 'place-location':
            form = CutPlaceLocationForm(request.POST or None)
            form1 = PlaceMapCoordinatesForm(request.POST or None)
        if attribute == 'school-location':
            form = CutSchoolLocationForm(request.POST or None)
            form1 = SchoolMapCoordinatesForm(request.POST or None)
        if attribute == 'organization-location':
            form = CutOrganizationLocationForm(request.POST or None)
            form1 = OrganizationMapCoordinatesForm(request.POST or None)
        if form.is_valid():
            coordinates = form1.save()
            location = form.save(commit=False)
            location.coordinates = coordinates
            location.save()
            return HttpResponseRedirect('/%s/edit/%s' %
                                        (request.GET.get('instance'),
                                         get_direction_city_parameter(city_title, direction_title)
                                         ))
        context = {
            'form': form,
            'form1': form1,
            'incoming_instance': request.GET.get('instance')

        }
        return render(request, html_template_path, context)
    if attribute == 'phone-number':
        form = PhoneNumberForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/%s/edit/%s' %
                                    (request.GET.get('instance'),
                                     get_direction_city_parameter(city_title, direction_title)
                                     ))
    context = {
        'form': form,
        'incoming_instance': request.GET.get('instance')

    }
    return render(request, html_template_path, context)
