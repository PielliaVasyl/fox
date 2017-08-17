from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from algoritms.get_direction_city_parameter import get_direction_city_parameter
from directions.all.forms import PlacesFilterForm
from entities.models import PlaceType

from entities.models.pages import Place
from entities.edit_forms.place import EditPlaceDirectionsForm, EditPlaceDescriptionForm, EditPlaceImageForm, \
    EditPlaceTypesForm, EditPlaceTitleForm, EditPlaceCitiesForm, EditPlaceLinksForm, EditPlacePlaceDanceClassesForm, \
    EditPlacePolicyForm, EditPlacePlaceLocationForm


def place(request, instance_id, direction_title=None, city_title=None):
    current_place = get_object_or_404(Place, pk=instance_id)
    title = '%s' % (current_place.title,)

    form = PlacesFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_place,
        'form': form
    }
    return render(request, 'entities/place/place-single.html', context)


def edit_place(request, instance_id, city_title=None, direction_title=None):
    instance = get_object_or_404(Place, pk=instance_id)
    title = '%s' % (instance.title,)

    edit_buttons = [
        ('place', 'title', 'Название'),
        ('place', 'directions', 'Направления'),
        ('place', 'cities', 'Города'),
        ('place', 'types', 'Типы мест'),
        ('place', 'place-dance-classes', 'Танцевальные стили и направления'),
        ('place', 'description', 'Описание'),
        ('place', 'image', 'Изобрадение'),
        ('place', 'video', 'Видео'),
        ('place', 'place-locations', 'Места проведения'),
        ('place', 'place-links', 'Ссылки'),
        ('place', 'policy', 'Права пользователей'),
    ]

    context = {
        'title': title,
        'instance': instance,
        'edit_buttons': edit_buttons
    }
    return render(request, 'entities/place/place-edit.html', context)


def edit_place_attr(request, instance_id, attribute=None, city_title=None, direction_title=None):
    instance = get_object_or_404(Place, pk=instance_id)
    title = '%s' % (instance.title,)

    attr = attribute
    html_template_path = 'entities/place/edit/edit-' + attribute + '.html'

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
        return HttpResponseRedirect('/place-%s/edit/%s' %
                                    (instance.pk, get_direction_city_parameter(city_title, direction_title)))

    context = {
        'title': title,
        'instance': instance,
        'form': form
    }
    return render(request, html_template_path, context)
