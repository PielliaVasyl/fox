from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from algoritms.get_direction_city_parameter import get_direction_city_parameter
from directions.all.forms import SchoolsFilterForm

from entities.models import SchoolContacts
from entities.models.pages import School
from entities.edit_forms.school import EditSchoolTitleForm, EditSchoolDirectionsForm, \
    EditSchoolSchoolDanceClassesForm, EditSchoolCitiesForm, EditSchoolDescriptionForm, EditSchoolImageForm, \
    EditSchoolSchoolLocationForm, EditSchoolLinksForm, EditSchoolPolicyForm, EditSchoolEmployeesForm, \
    EditSchoolSchoolContactForm, EditSchoolSocialsForm


def school(request, instance_id, direction_title=None, city_title=None):
    current_school = get_object_or_404(School, pk=instance_id)
    title = '%s' % (current_school.title,)

    form = SchoolsFilterForm(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_school,
        'form': form
    }
    return render(request, 'entities/school/school-single.html', context)


def edit_school(request, instance_id, city_title=None, direction_title=None):
    instance = get_object_or_404(School, pk=instance_id)
    title = '%s' % (instance.title,)

    edit_buttons = [
        ('school', 'title', 'Название'),
        ('school', 'directions', 'Направления'),
        ('school', 'cities', 'Города'),
        ('school', 'school-dance-classes', 'Танцевальные стили и направления'),
        ('school', 'description', 'Описание'),
        ('school', 'image', 'Изобрадение'),
        ('school', 'school-locations', 'Места'),
        ('school', 'employees', 'Сотрудники'),
        ('school', 'school-links', 'Ссылки'),
        ('school', 'school-contacts', 'Контакты'),
        ('school', 'policy', 'Права пользователей'),
    ]

    context = {
        'title': title,
        'instance': instance,
        'edit_buttons': edit_buttons
    }
    return render(request, 'entities/school/school-edit.html', context)


def edit_school_attr(request, instance_id, attribute=None, city_title=None, direction_title=None):
    instance = get_object_or_404(School, pk=instance_id)
    title = '%s' % (instance.title,)

    attr = attribute
    html_template_path = 'entities/school/edit/edit-' + attribute + '.html'

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
            return HttpResponseRedirect('/school-%s/edit/%s' %
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
        return HttpResponseRedirect('/school-%s/edit/%s' %
                                    (instance.pk, get_direction_city_parameter(city_title, direction_title)))

    context = {
        'title': title,
        'instance': instance,
        'form': form
    }
    return render(request, html_template_path, context)
