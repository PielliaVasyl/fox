from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from algoritms.get_direction_city_parameter import get_direction_city_parameter
from directions.all.forms import EventsFilterForm, PromoActionsFilterForm, PlacesFilterForm, SchoolsFilterForm

from entities.models import DayOfTheWeek
from entities.models import EventType
from entities.models import ExperienceLevel
from entities.models import Organization
from entities.models import Place
from entities.models import PlaceType
from entities.models import PriceType
from entities.models import RepeatsType
from entities.models import School
from entities.models import SchoolContacts
from entities.models import Socials
from entities.models import Teacher
from entities.models.events import Event, PromoAction
from entities.views.event import EVENT_EDIT_BUTTONS, EVENT_ATTRIBUTE_FORMS
from entities.views.place import PLACE_EDIT_BUTTONS, PLACE_ATTRIBUTE_FORMS
from entities.views.promo_action import PROMO_ACTION_EDIT_BUTTONS, PROMO_ACTION_ATTRIBUTE_FORMS
from entities.views.school import SCHOOL_EDIT_BUTTONS, SCHOOL_ATTRIBUTE_FORMS
from entities.views.teacher import TEACHER_EDIT_BUTTONS

ENTITY = {
    'event': Event,
    'promo-action': PromoAction,
    'place': Place,
    'school': School,
    'teacher': Teacher,
    'organization': Organization
}

ENTITY_FORM = {
    'event': EventsFilterForm,
    'promo-action': PromoActionsFilterForm,
    'place': PlacesFilterForm,
    'school': SchoolsFilterForm,
    # 'teacher': TeachersFilterForm,
    # 'organization': OrganizationsFilterForm,
}

EDIT_BUTTONS = {
    'event': EVENT_EDIT_BUTTONS,
    'promo-action': PROMO_ACTION_EDIT_BUTTONS,
    'place': PLACE_EDIT_BUTTONS,
    'school': SCHOOL_EDIT_BUTTONS,
    'teacher':  TEACHER_EDIT_BUTTONS,
    # 'organization': ORGANIZATION_EDIT_BUTTONS
}

ATTRIBUTE_FORMS = {
    'event': EVENT_ATTRIBUTE_FORMS,
    'promo-action': PROMO_ACTION_ATTRIBUTE_FORMS,
    'place': PLACE_ATTRIBUTE_FORMS,
    'school': SCHOOL_ATTRIBUTE_FORMS,
    # 'teacher':  TEACHER_ATTRIBUTE_FORMS,
    # 'organization': ORGANIZATION_FORMS,
}


def show_instance(request, entity, instance_id, direction_title=None, city_title=None):
    html_template_path = 'entities/%s/%s-single.html' % (entity.replace('-', '_'), entity)

    current_entity = ENTITY.get(entity, None)
    current_instance = get_object_or_404(current_entity, pk=instance_id)
    title = '%s' % (current_instance.title,)

    form = ENTITY_FORM.get(entity, None)
    if form is not None:
        form = form(request.POST or None, direction=direction_title)

    context = {
        'title': title,
        'instance': current_instance,
        'form': form
    }
    return render(request, html_template_path, context)


def edit_instance(request, entity, instance_id, city_title=None, direction_title=None):
    html_template_path = 'entities/%s/%s-edit.html' % (entity.replace('-', '_'), entity)

    current_entity = ENTITY.get(entity, None)
    current_instance = get_object_or_404(current_entity, pk=instance_id)
    title = '%s' % (current_instance.title,)

    edit_buttons = EDIT_BUTTONS.get(entity, None)

    context = {
        'title': title,
        'instance': current_instance,
        'edit_buttons': edit_buttons
    }
    return render(request, html_template_path, context)


def __get_form(entity, attribute, request, current_instance):
    form = None
    attribute_forms = ATTRIBUTE_FORMS.get(entity, None)
    if attribute_forms:
        form = attribute_forms.get(attribute, None)

    if form:
        if attribute in ['title', 'description', 'note', 'video', 'repeats-type']:
            form = form(request.POST or None,
                        initial={attribute.replace("-", "_"):
                                 getattr(current_instance, attribute.replace("-", "_"), None)})
        if attribute in ['directions', 'cities', 'types', 'schedule', 'price-types', 'experience-levels', 'employees']:
            form = form(request.POST or None,
                        initial={attribute.replace("-", "_"):
                                 getattr(current_instance, attribute.replace("-", "_"), None).all()})
        if attribute == 'image':
            if request.method == 'POST':
                form = form(request.POST, request.FILES)
            else:
                form = form(None, initial={attribute: getattr(current_instance, attribute.replace("-", "_"), None)})
        if attribute == 'dates':
            form = form(request.POST or None, initial={'start_date': current_instance.start_date,
                                                       'end_date': current_instance.end_date})
        if attribute == 'status':
            form = form(request.POST or None, initial={'_status': current_instance._status})
        if attribute in ['event-locations', 'place-locations', 'school-locations']:
            form = form(request.POST or None, initial={'locations': current_instance.locations.all()})
        if attribute in ['event-links', 'promo-action-links', 'place-links', 'school-links']:
            form = form(request.POST or None, initial={'links': current_instance.links.all()})
        if attribute in ['event-dance-classes', 'promo-action-dance-classes', 'place-dance-classes',
                         'school-dance-classes']:
            form = form(request.POST or None, initial={'dance_directions':
                                                       current_instance.local_classes.dance_directions.all(),
                                                       'dance_styles':
                                                       current_instance.local_classes.dance_styles.all()})
        if attribute == 'contacts':
            form = form(request.POST or None, initial={'phone_numbers': current_instance.contacts.phone_numbers.all()})
        if attribute == 'socials':
            form = form(request.POST or None, initial={'fb': current_instance.contacts.socials.fb.all(),
                                                       'vk': current_instance.contacts.socials.vk.all(),
                                                       'instagram': current_instance.contacts.socials.instagram.all(),
                                                       'twitter': current_instance.contacts.socials.twitter.all()})
        if attribute == 'policy':
            form = form(request.POST or None, initial={'owners': current_instance.owners.all(),
                                                       'contributors': current_instance.contributors.all(),
                                                       'author': current_instance.author})
    return form


def set_attributes(current_instance, attr_values):
    for attr, value in attr_values.items():
        if attr in ['dance_styles', 'dance_directions']:
            setattr(current_instance.local_classes, attr, value)
        else:
            setattr(current_instance, attr.replace('-', '_'), value)


def save_instance_changes(entity, form, attribute, request, current_instance):
    attr_values = {}
    if attribute in ['title', 'directions', 'cities', 'description', 'note', 'video', 'employees']:
        attr_values[attribute] = form.cleaned_data.get(attribute)
    if attribute == 'image':
        if 'image' in request.FILES:
            value = request.FILES['image']
        else:
            value = None
        attr_values[attribute] = value
    if attribute == 'dates':
        attr_values['start_date'] = form.cleaned_data.get('start_date')
        attr_values['end_date'] = form.cleaned_data.get('end_date')
    if attribute in ['event-dance-classes', 'promo-action-dance-classes', 'place-dance-classes',
                     'school-dance-classes']:
        attr_values['dance_styles'] = form.cleaned_data.get('dance_styles')
        attr_values['dance_directions'] = form.cleaned_data.get('dance_directions')
    if attribute == 'types' and entity == 'event':
        attr_values[attribute] = EventType.objects.filter(title__in=form.cleaned_data.get(attribute))
    if attribute == 'types' and entity == 'place':
        attr_values[attribute] = PlaceType.objects.filter(title__in=form.cleaned_data.get(attribute))
    if attribute == 'price-types':
        attr_values[attribute] = PriceType.objects\
            .filter(title__in=form.cleaned_data.get(attribute.replace('-', '_')))
    if attribute == 'experience-levels':
        attr_values[attribute] = ExperienceLevel.objects\
            .filter(title__in=form.cleaned_data.get(attribute.replace('-', '_')))
    if attribute == 'repeats-type':
        attr_values[attribute] = RepeatsType.objects\
            .filter(title=form.cleaned_data.get(attribute.replace('-', '_'))).first()
    if attribute == 'schedule':
        attr_values[attribute] = DayOfTheWeek.objects.filter(title__in=form.cleaned_data.get(attribute))
    if attribute == 'status':
        attr_values['_status'] = form.cleaned_data.get('_status')
    if attribute in ['event-locations', 'place-locations', 'school-locations']:
        attr_values['locations'] = form.cleaned_data.get('locations')
    if attribute in ['event-links', 'promo-action-links', 'place-links', 'school-links']:
        attr_values['links'] = form.cleaned_data.get('links')
    if attribute == 'policy':
        attr_values['owners'] = form.cleaned_data.get('owners')
        attr_values['contributors'] = form.cleaned_data.get('contributors')
        attr_values['author'] = form.cleaned_data.get('author')

    set_attributes(current_instance, attr_values)
    current_instance.save()


def _get_response_redirect(entity, instance_id, city_title, direction_title):
    return '/%s-%s/edit/%s' % (entity,
                               instance_id,
                               get_direction_city_parameter(city_title, direction_title))


def edit_instance_attr(request, entity, instance_id, attribute=None, city_title=None, direction_title=None):
    current_entity = ENTITY.get(entity, None)
    current_instance = get_object_or_404(current_entity, pk=instance_id)
    title = '%s' % (current_instance.title,)
    html_template_path = 'entities/%s/edit/edit-%s.html' % (entity.replace('-', '_'), attribute)

    if attribute == 'school-contacts':
        form_contact = __get_form(entity, 'contacts', request, current_instance)
        form_socials = __get_form(entity, 'socials', request, current_instance)

        if form_contact.is_valid():
            contacts = SchoolContacts.objects.get(author_id=current_instance.author_id)
            set_attributes(contacts, {'phone_numbers': form_contact.cleaned_data.get('phone_numbers')})
            set_attributes(current_instance, {'contacts': contacts})
            current_instance.save()
        if form_socials.is_valid():
            attr_values = {'fb': form_contact.cleaned_data.get('fb'),
                           'vk': form_contact.cleaned_data.get('vk'),
                           'twitter': form_contact.cleaned_data.get('twitter'),
                           'instagram': form_contact.cleaned_data.get('instagram')}
            socials = Socials.objects.get(author_id=current_instance.author_id)
            set_attributes(socials, attr_values)
            set_attributes(current_instance, {'socials': socials})
            current_instance.save()
        if any([form_contact.is_valid(), form_socials.is_valid()]):
            return HttpResponseRedirect(_get_response_redirect(entity, instance_id, city_title, direction_title))

        context = {
            'form_contact': form_contact,
            'form_socials': form_socials
        }
    else:
        form = __get_form(entity, attribute, request, current_instance)

        if form.is_valid():
            save_instance_changes(entity, form, attribute, request, current_instance)

            return HttpResponseRedirect(_get_response_redirect(entity, instance_id, city_title, direction_title))

        context = {
            'form': form
        }

    context['instance'] = current_instance
    context['title'] = title

    return render(request, html_template_path, context)
