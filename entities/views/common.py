# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from directions.all.forms import EventsFilterForm, PromoActionsFilterForm, PlacesFilterForm, SchoolsFilterForm, \
    ShopsFilterForm, CustomerServicesFilterForm, HallsFilterForm
from entities.forms.contacts import PhoneNumberForm
from entities.forms.classes import DirectionForm, CityForm
from entities.forms.links import EventLinkForm, PromoActionLinkForm, PlaceLinkForm, SchoolLinkForm, TeacherLinkForm, \
    ShopLinkForm, CustomerServicesLinkForm, HallLinkForm, OrganizationLinkForm, PersonLinkForm, ResourceLinkForm
from entities.forms.locations import EventLocationForm, CutPlaceLocationForm, PlaceMapCoordinatesForm, \
    SchoolMapCoordinatesForm, CutSchoolLocationForm, OrganizationMapCoordinatesForm, CutOrganizationLocationForm, \
    ShopMapCoordinatesForm, CutShopLocationForm, CutHallLocationForm, HallMapCoordinatesForm, \
    CutCustomerServicesLocationForm, CustomerServicesMapCoordinatesForm
from entities.forms.tags import ArticleTagForm, ChapterTagForm, AlbumTagForm, PlaylistTagForm, TracklistTagForm, \
    DanceDirectionTagForm, PhotoTagForm, VideoTagForm, AudioTagForm, DanceStyleTagForm
from entities.models.contacts import OrganizationContacts, SchoolContacts, TeacherContacts, PersonContacts, \
    ShopContacts, CustomerServicesContacts, HallContacts, ResourceContacts, Socials
from entities.models.events import Event, PromoAction
from entities.models.links import DanceStyleAuthorLink
from entities.models.pages import Place, School, Organization, Teacher, Person, Shop, CustomerServices, Hall, Resource
from entities.models.posts import Article, Playlist, Audio, Tracklist, DanceStyle, DanceDirection, Chapter, Photo, \
    Album, Video
from entities.models.types import ShopType, CustomerServicesType, DayOfTheWeek, EventType, ExperienceLevel, \
    PlaceType, PriceType, RepeatsType
from entities.models.userprofile import UserProfile
from entities.views.album import ALBUM_EDIT_BUTTONS, ALBUM_ATTRIBUTE_FORMS
from entities.views.article import ARTICLE_EDIT_BUTTONS, ARTICLE_ATTRIBUTE_FORMS
from entities.views.audio import AUDIO_EDIT_BUTTONS, AUDIO_ATTRIBUTE_FORMS
from entities.views.chapter import CHAPTER_EDIT_BUTTONS, CHAPTER_ATTRIBUTE_FORMS
from entities.views.customer_services import CUSTOMER_SERVICES_EDIT_BUTTONS, CUSTOMER_SERVICES_ATTRIBUTE_FORMS
from entities.views.dance_direction import DANCE_DIRECTION_EDIT_BUTTONS, DANCE_DIRECTION_ATTRIBUTE_FORMS
from entities.views.dance_style import DANCE_STYLE_EDIT_BUTTONS, DANCE_STYLE_ATTRIBUTE_FORMS
from entities.views.event import EVENT_EDIT_BUTTONS, EVENT_ATTRIBUTE_FORMS
from entities.views.hall import HALL_EDIT_BUTTONS, HALL_ATTRIBUTE_FORMS
from entities.views.organization import ORGANIZATION_EDIT_BUTTONS, ORGANIZATION_ATTRIBUTE_FORMS
from entities.views.person import PERSON_EDIT_BUTTONS, PERSON_ATTRIBUTE_FORMS
from entities.views.photo import PHOTO_EDIT_BUTTONS, PHOTO_ATTRIBUTE_FORMS
from entities.views.place import PLACE_EDIT_BUTTONS, PLACE_ATTRIBUTE_FORMS
from entities.views.playlist import PLAYLIST_EDIT_BUTTONS, PLAYLIST_ATTRIBUTE_FORMS
from entities.views.profiles import PROFILE_EDIT_BUTTONS, PROFILE_ATTRIBUTE_FORMS
from entities.views.promo_action import PROMO_ACTION_EDIT_BUTTONS, PROMO_ACTION_ATTRIBUTE_FORMS
from entities.views.resource import RESOURCE_EDIT_BUTTONS, RESOURCE_ATTRIBUTE_FORMS
from entities.views.school import SCHOOL_EDIT_BUTTONS, SCHOOL_ATTRIBUTE_FORMS
from entities.views.shop import SHOP_EDIT_BUTTONS, SHOP_ATTRIBUTE_FORMS
from entities.views.teacher import TEACHER_EDIT_BUTTONS, TEACHER_ATTRIBUTE_FORMS
from entities.views.tracklist import TRACKLIST_EDIT_BUTTONS, TRACKLIST_ATTRIBUTE_FORMS
from entities.views.video import VIDEO_EDIT_BUTTONS, VIDEO_ATTRIBUTE_FORMS

ENTITY = {
    'event': Event,
    'promo-action': PromoAction,
    'place': Place,
    'school': School,
    'teacher': Teacher,
    'organization': Organization,
    'person': Person,
    'shop': Shop,
    'customer-services': CustomerServices,
    'hall': Hall,
    'resource': Resource,
    'article': Article,
    'chapter': Chapter,
    'photo': Photo,
    'album': Album,
    'video': Video,
    'playlist': Playlist,
    'audio': Audio,
    'tracklist': Tracklist,
    'dance-style': DanceStyle,
    'dance-direction': DanceDirection,
    'profile': UserProfile
}

ENTITY_FILTER_FORM = {
    'event': EventsFilterForm,
    'promo-action': PromoActionsFilterForm,
    'place': PlacesFilterForm,
    'school': SchoolsFilterForm,
    # 'teacher': TeachersFilterForm,
    # 'organization': OrganizationsFilterForm,
    'shop': ShopsFilterForm,
    'customer-services': CustomerServicesFilterForm,
    'hall': HallsFilterForm,
    # 'resource': ResourceFilterForm
}

EDIT_BUTTONS = {
    'event': EVENT_EDIT_BUTTONS,
    'promo-action': PROMO_ACTION_EDIT_BUTTONS,
    'place': PLACE_EDIT_BUTTONS,
    'school': SCHOOL_EDIT_BUTTONS,
    'teacher':  TEACHER_EDIT_BUTTONS,
    'organization': ORGANIZATION_EDIT_BUTTONS,
    'person': PERSON_EDIT_BUTTONS,
    'shop': SHOP_EDIT_BUTTONS,
    'customer-services': CUSTOMER_SERVICES_EDIT_BUTTONS,
    'hall': HALL_EDIT_BUTTONS,
    'resource': RESOURCE_EDIT_BUTTONS,
    'article': ARTICLE_EDIT_BUTTONS,
    'chapter': CHAPTER_EDIT_BUTTONS,
    'photo': PHOTO_EDIT_BUTTONS,
    'album': ALBUM_EDIT_BUTTONS,
    'video': VIDEO_EDIT_BUTTONS,
    'playlist': PLAYLIST_EDIT_BUTTONS,
    'audio': AUDIO_EDIT_BUTTONS,
    'tracklist': TRACKLIST_EDIT_BUTTONS,
    'dance-style': DANCE_STYLE_EDIT_BUTTONS,
    'dance-direction': DANCE_DIRECTION_EDIT_BUTTONS,
    'profile': PROFILE_EDIT_BUTTONS
}

ATTRIBUTE_FORMS = {
    'event': EVENT_ATTRIBUTE_FORMS,
    'promo-action': PROMO_ACTION_ATTRIBUTE_FORMS,
    'place': PLACE_ATTRIBUTE_FORMS,
    'school': SCHOOL_ATTRIBUTE_FORMS,
    'teacher':  TEACHER_ATTRIBUTE_FORMS,
    'organization': ORGANIZATION_ATTRIBUTE_FORMS,
    'person': PERSON_ATTRIBUTE_FORMS,
    'shop': SHOP_ATTRIBUTE_FORMS,
    'customer-services': CUSTOMER_SERVICES_ATTRIBUTE_FORMS,
    'hall': HALL_ATTRIBUTE_FORMS,
    'resource': RESOURCE_ATTRIBUTE_FORMS,
    'article': ARTICLE_ATTRIBUTE_FORMS,
    'chapter': CHAPTER_ATTRIBUTE_FORMS,
    'photo': PHOTO_ATTRIBUTE_FORMS,
    'album': ALBUM_ATTRIBUTE_FORMS,
    'video': VIDEO_ATTRIBUTE_FORMS,
    'playlist': PLAYLIST_ATTRIBUTE_FORMS,
    'audio': AUDIO_ATTRIBUTE_FORMS,
    'tracklist': TRACKLIST_ATTRIBUTE_FORMS,
    'dance-style': DANCE_STYLE_ATTRIBUTE_FORMS,
    'dance-direction': DANCE_DIRECTION_ATTRIBUTE_FORMS,
    'profile': PROFILE_ATTRIBUTE_FORMS
}

CONTACTS_ENTITY = {
    'school': SchoolContacts,
    'teacher':  TeacherContacts,
    'organization': OrganizationContacts,
    'person': PersonContacts,
    'shop': ShopContacts,
    'customer-services': CustomerServicesContacts,
    'hall': HallContacts,
    'resource': ResourceContacts
}


def _get_title(current_instance):
    if hasattr(current_instance, 'title'):
        title = '%s' % (current_instance.title,)
    else:
        title = '%s' % (current_instance.user.username,)
    return title


def instance_page(request, entity, instance_id):
    html_template_path = 'entities/%s/%s-single.html' % (entity.replace('-', '_'), entity)

    current_entity = ENTITY.get(entity, None)
    current_instance = get_object_or_404(current_entity, pk=instance_id)
    title = _get_title(current_instance)

    form = ENTITY_FILTER_FORM.get(entity, None)
    if form is not None:
        form = form(request.POST or None, direction=None)

    context = {
        'title': title,
        'instance': current_instance,
        'form': form
    }
    return render(request, html_template_path, context)


def edit_instance_page(request, entity, instance_id):
    html_template_path = 'entities/%s/%s-edit.html' % (entity.replace('-', '_'), entity)

    current_entity = ENTITY.get(entity, None)
    current_instance = get_object_or_404(current_entity, pk=instance_id)
    title = _get_title(current_instance)

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
        if attribute in ['directions', 'cities', 'types', 'schedule', 'price-types', 'experience-levels', 'employees',
                         'employers']:
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
        if '-locations' in attribute:
            form = form(request.POST or None, initial={'locations': current_instance.locations.all()})
        if '-links' in attribute:
            form = form(request.POST or None, initial={'links': current_instance.links.all()})
        if '-dance-classes' in attribute:
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
        if '-tags' in attribute:
            form = form(request.POST or None, initial={'tags': current_instance.tags.all()})
        if attribute in ['article-link', 'photo-link', 'video-link', 'audio-link', 'playlist-link']:
            form = form(request.POST or None, initial={'link': current_instance.link.link})
        if attribute in ['article-linked']:
            form = form(request.POST or None, initial={'is_linked_article': current_instance.is_linked_article})
        if attribute == 'article-description':
            form = form(request.POST or None, initial={'description': current_instance.description,
                                                       'author_of_post': current_instance.author_of_post})
        if '-groups' in attribute:
            form = form(request.POST or None, initial={'groups': current_instance.groups.all()})
        if attribute == 'dance-style-description':
            form = form(request.POST or None, initial={'description': current_instance.description,
                                                       'author_of_post': current_instance.author_of_post})
        if attribute == 'dance-style-link':
            form = form(request.POST or None, initial={'link': current_instance.link_to_author.link})
        if attribute == 'dance-style-group':
            form = form(request.POST or None, initial={'group': current_instance.group})
        if attribute == 'dance-style-count-types':
            form = form(request.POST or None, initial={'count_types': current_instance.count_types.all()})
        if attribute == 'dance-style-distance-types':
            form = form(request.POST or None, initial={'distance_types': current_instance.distance_types.all()})
        if attribute == 'name' and entity == 'profile':
            form = form(request.POST or None, initial={'username': current_instance.user.username})
    return form


def set_attributes(current_instance, attr_values):
    for attr, value in attr_values.items():
        if attr in ['dance_styles', 'dance_directions']:
            setattr(current_instance.local_classes, attr, value)
        elif attr in ['fb', 'vk', 'twitter', 'instagram']:
            if attr == 'fb':
                current_instance.fb.clear()
                if value:
                    current_instance.fb.add(value)
            if attr == 'vk':
                current_instance.vk.clear()
                if value:
                    current_instance.vk.add(value)
            if attr == 'twitter':
                current_instance.twitter.clear()
                if value:
                    current_instance.twitter.add(value)
            if attr == 'instagram':
                current_instance.instagram.clear()
                if value:
                    current_instance.instagram.add(value)
        elif attr in ['article-link', 'photo-link', 'video-link', 'audio-link', 'playlist-link']:
            current_instance.link = value
        else:
            setattr(current_instance, attr.replace('-', '_'), value)


def save_instance_changes(entity, form, attribute, request, current_instance):
    attr_values = {}
    if attribute in ['title', 'directions', 'cities', 'description', 'note', 'video', 'employees', 'employers']:
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
    if '-dance-classes' in attribute:
        attr_values['dance_styles'] = form.cleaned_data.get('dance_styles')
        attr_values['dance_directions'] = form.cleaned_data.get('dance_directions')
    if attribute == 'types' and entity == 'event':
        attr_values[attribute] = EventType.objects.filter(title__in=form.cleaned_data.get(attribute))
    if attribute == 'types' and entity == 'place':
        attr_values[attribute] = PlaceType.objects.filter(title__in=form.cleaned_data.get(attribute))
    if attribute == 'types' and entity == 'shop':
        attr_values[attribute] = ShopType.objects.filter(title__in=form.cleaned_data.get(attribute))
    if attribute == 'types' and entity == 'customer-services':
        attr_values[attribute] = CustomerServicesType.objects.filter(title__in=form.cleaned_data.get(attribute))
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
    if '-locations' in attribute:
        attr_values['locations'] = form.cleaned_data.get('locations')
    if '-links' in attribute:
        attr_values['links'] = form.cleaned_data.get('links')
    if attribute == 'policy':
        attr_values['owners'] = form.cleaned_data.get('owners')
        attr_values['contributors'] = form.cleaned_data.get('contributors')
        attr_values['author'] = form.cleaned_data.get('author')
    if '-tags' in attribute:
        attr_values['tags'] = form.cleaned_data.get('tags')
    if attribute == 'article-description':
        attr_values['description'] = form.cleaned_data.get('description')
        attr_values['author_of_post'] = form.cleaned_data.get('author_of_post')
    if attribute in ['article-link', 'photo-link', 'video-link', 'audio-link', 'playlist-link']:
        current_instance = current_instance.link
        attr_values[attribute] = form.cleaned_data.get('link')
    if attribute == 'article-linked':
        attr_values['is_linked_article'] = form.cleaned_data.get('is_linked_article')
    if attribute == 'article-groups':
        attr_values['groups'] = form.cleaned_data.get('groups')
    if attribute == 'dance-style-count-types':
        attr_values['count_types'] = form.cleaned_data.get('count_types')
    if attribute == 'dance-style-distance-types':
        attr_values['distance_types'] = form.cleaned_data.get('distance_types')
    if attribute == 'name' and entity == 'profile':
        attr_values['username'] = form.cleaned_data.get('username')
        current_instance = current_instance.user

    set_attributes(current_instance, attr_values)
    current_instance.save()


def _get_response_redirect(entity, instance_id):
    return '/%s-%s/edit/' % (entity,
                             instance_id)


def _get_contacts(entity, author_id, instance_id):
    contacts_entity = CONTACTS_ENTITY.get(entity, None)
    if contacts_entity:
        contacts = eval('contacts_entity.objects.get(author_id=%s, %s__id=%s)'
                        % (author_id, entity.replace('-', ''), instance_id))
        return contacts
    return None


def _get_socials(entity, author_id, instance_id):
    socials = eval('Socials.objects.get(author_id=%s, %scontacts__%s__id=%s)'
                   % (author_id, entity.replace('-', ''), entity.replace('-', ''), instance_id))
    return socials


def _get_modal_window_title(attribute):
    modal_window_title = {
        'title': 'Изменить название',
        'article-groups': 'Изменить список глав',
    }.get(attribute, '!mod_win_title')
    return modal_window_title


def _get_modal_window_add_entity(attribute):
    modal_window_add_entity = {
        'article-groups': 'chapter',
        # ''
    }.get(attribute, '!mod_win_add_ent')
    return modal_window_add_entity


def _get_modal_window_add_entity_btn(attribute):
    modal_window_add_entity_btn = {
        'article-groups': 'Добавить новую главу',
    }.get(attribute, '!mod_win_add_ent_tit')
    return modal_window_add_entity_btn


def _get_html_template_path(attribute):
    attr_template = {
        'cities': 'attr-2',
        'directions': 'attr-2',

        'event-links': 'attr-2',
        'promo-action-links': 'attr-2',
        'place-links': 'attr-2',
        'school-links': 'attr-2',
        'teacher-links': 'attr-2',
        'organization-links': 'attr-2',
        'person-links': 'attr-2',
        'shop-links': 'attr-2',
        'customer-services-links': 'attr-2',
        'hall-links': 'attr-2',
        'resource-links': 'attr-2',

        'event-locations': 'attr-2',
        'place-locations': 'attr-2',
        'school-locations': 'attr-2',
        'teacher-locations': 'attr-2',
        'organization-locations': 'attr-2',
        'shop-locations': 'attr-2',
        'customer-services-locations': 'attr-2',
        'hall-locations': 'attr-2',

        'article-tags': 'attr-2',
        'album-tags': 'attr-2',
        'audio-tags': 'attr-2',
        'chapter-tags': 'attr-2',
        'dance-direction-tags': 'attr-2',
        'dance-style-tags': 'attr-2',
        'photo-tags': 'attr-2',
        'playlist-tags': 'attr-2',
        'video-tags': 'attr-2',

        'employees': 'attr-3-employees',
        'employers': 'attr-3-employers',

        'school-contacts': 'attr-4-contacts',
        'teacher-contacts': 'attr-4-contacts',
        'organization-contacts': 'attr-4-contacts',
        'person-contacts': 'attr-4-contacts',
        'shop-contacts': 'attr-4-contacts',
        'customer-services-contacts': 'attr-4-contacts',
        'hall-contacts': 'attr-4-contacts',
        'resource-contacts': 'attr-4-contacts',

        'article-groups': 'attr-5-groups'

    }.get(attribute, 'attr')
    html_template_path = 'attrs/edit/edit-%s.html' % (attr_template,)
    return html_template_path


def _get_create_attribute_title(attribute):
    create_attribute_title = {
        'cities': 'Добавить новый город',
        'city': 'Добавить новый город',
        'directions': 'Добавить новое направление',
        'direction': 'Добавить новое направление',
        'phone-number': 'Добавить новый номер телефона',

        'event-links': 'Добавить новую ссылку',
        'event-link': 'Добавить новую ссылку',
        'customer-services-links': 'Добавить новую ссылку',
        'customer-services-link': 'Добавить новую ссылку',
        'hall-links': 'Добавить новую ссылку',
        'hall-link': 'Добавить новую ссылку',
        'organization-links': 'Добавить новую ссылку',
        'organization-link': 'Добавить новую ссылку',
        'person-links': 'Добавить новую ссылку',
        'person-link': 'Добавить новую ссылку',
        'place-links': 'Добавить новую ссылку',
        'place-link': 'Добавить новую ссылку',
        'promo-action-links': 'Добавить новую ссылку',
        'promo-action-link': 'Добавить новую ссылку',
        'resource-links': 'Добавить новую ссылку',
        'resource-link': 'Добавить новую ссылку',
        'school-links': 'Добавить новую ссылку',
        'school-link': 'Добавить новую ссылку',
        'shop-links': 'Добавить новую ссылку',
        'shop-link': 'Добавить новую ссылку',
        'teacher-links': 'Добавить новую ссылку',
        'teacher-link': 'Добавить новую ссылку',

        'event-locations': 'Добавить новое место проведения',
        'event-location': 'Добавить новое место проведения',
        'customer-services-locations': 'Добавить новое место проведения',
        'customer-services-location': 'Добавить новое место проведения',
        'hall-locations': 'Добавить новое место проведения',
        'hall-location': 'Добавить новое место проведения',
        'organization-locations': 'Добавить новое место проведения',
        'organization-location': 'Добавить новое место проведения',
        'place-locations': 'Добавить новое место проведения',
        'place-location': 'Добавить новое место проведения',
        'school-locations': 'Добавить новое место проведения',
        'school-location': 'Добавить новое место проведения',
        'shop-locations': 'Добавить новое место проведения',
        'shop-location': 'Добавить новое место проведения',

        'album-tags': 'Добавить новый тег',
        'album-tag': 'Добавить новый тег',
        'article-tags': 'Добавить новый тег',
        'article-tag': 'Добавить новый тег',
        'audio-tags': 'Добавить новый тег',
        'audio-tag': 'Добавить новый тег',
        'chapter-tags': 'Добавить новый тег',
        'chapter-tag': 'Добавить новый тег',
        'dance-direction-tags': 'Добавить новый тег',
        'dance-direction-tag': 'Добавить новый тег',
        'dance-style-tags': 'Добавить новый тег',
        'dance-style-tag': 'Добавить новый тег',
        'photo-tags': 'Добавить новый тег',
        'photo-tag': 'Добавить новый тег',
        'playlist-tags': 'Добавить новый тег',
        'playlist-tag': 'Добавить новый тег',
        'video-tags': 'Добавить новый тег',
        'video-tag': 'Добавить новый тег',

    }.get(attribute, '!cr_attr_title')
    return create_attribute_title


def _get_create_attribute(attribute):
    create_attribute = {
        'cities': 'city',
        'directions': 'direction',
        'event-links': 'event-link',
        'promo-action-links': 'promo-action-link',
        'place-links': 'place-link',
        'school-links': 'school-link',
        'teacher-links': 'teacher-link',
        'organization-links': 'organization-link',
        'person-links': 'person-link',
        'shop-links': 'shop-link',
        'customer-services-links': 'customer-services-link',
        'hall-links': 'hall-link',
        'resource-links': 'resource-link',

        'event-locations': 'event-location',
        'place-locations': 'place-location',
        'school-locations': 'school-location',
        'organization-locations': 'organization-location',
        'shop-locations': 'shop-location',
        'customer-services-locations': 'customer-services-location',
        'hall-locations': 'hall-location',

        'article-tags': 'article-tag',
        'album-tags': 'album-tag',
        'audio-tags': 'audio-tag',
        'chapter-tags': 'chapter-tag',
        'dance-direction-tags': 'dance-direction-tag',
        'dance-style-tags': 'dance-style-tag',
        'photo-tags': 'photo-tag',
        'playlist-tags': 'playlist-tag',
        'video-tags': 'video-tag',

    }.get(attribute, '!cr_attr')
    return create_attribute


def edit_instance_attr(request, entity, instance_id, attribute=None):
    current_entity = ENTITY.get(entity, None)
    current_instance = get_object_or_404(current_entity, pk=instance_id)
    title = _get_title(current_instance)
    html_template_path = _get_html_template_path(attribute)

    if '-contacts' in attribute:
        form_contact = __get_form(entity, 'contacts', request, current_instance)
        form_socials = __get_form(entity, 'socials', request, current_instance)
        if form_contact.is_valid():
            contacts = _get_contacts(entity=entity, author_id=current_instance.author_id, instance_id=instance_id)
            set_attributes(contacts, {'phone_numbers': form_contact.cleaned_data.get('phone_numbers')})
            set_attributes(current_instance, {'contacts': contacts})
            current_instance.save()
        if form_socials.is_valid():
            attr_values = {'fb': form_contact.cleaned_data.get('fb'),
                           'vk': form_contact.cleaned_data.get('vk'),
                           'twitter': form_contact.cleaned_data.get('twitter'),
                           'instagram': form_contact.cleaned_data.get('instagram')}
            socials = _get_socials(entity=entity, author_id=current_instance.author_id, instance_id=instance_id)
            set_attributes(socials, attr_values)
            set_attributes(current_instance, {'socials': socials})
            current_instance.save()
        if any([form_contact.is_valid(), form_socials.is_valid()]):
            return HttpResponseRedirect(_get_response_redirect(entity, instance_id))

        context = {
            'form_contact': form_contact,
            'form_socials': form_socials
        }
    elif attribute == 'dance-style-description':
        form_description = __get_form(entity, 'dance-style-description', request, current_instance)
        form_dance_style_link = __get_form(entity, 'dance-style-link', request, current_instance)
        if form_description.is_valid():
            attr_values = {'description': form_description.cleaned_data.get('description'),
                           'author_of_post': form_description.cleaned_data.get('author_of_post')}
            set_attributes(current_instance, attr_values)
            current_instance.save()
        if form_dance_style_link.is_valid():
            link_to_author = DanceStyleAuthorLink.objects.get(author_id=current_instance.author_id,
                                                              dancestyle__id=instance_id)
            set_attributes(link_to_author, {'link': form_dance_style_link.cleaned_data.get('link')})
            link_to_author.save()
        if any([form_description.is_valid(), form_dance_style_link.is_valid()]):
            return HttpResponseRedirect(_get_response_redirect(entity, instance_id))

        context = {
            'form_description': form_description,
            'form_dance_style_link': form_dance_style_link
        }
    else:
        form = __get_form(entity, attribute, request, current_instance)

        if form.is_valid():
            save_instance_changes(entity, form, attribute, request, current_instance)

            return HttpResponseRedirect(_get_response_redirect(entity, instance_id))

        context = {
            'form': form
        }
    if '-groups' in attribute:
        context['modal_window_add_entity'] = _get_modal_window_add_entity(attribute)
        context['modal_window_add_entity_btn'] = _get_modal_window_add_entity_btn(attribute)
    context['create_attribute_title'] = _get_create_attribute_title(attribute)
    context['create_attribute'] = _get_create_attribute(attribute)
    context['modal_window_title'] = _get_modal_window_title(attribute)
    context['attribute'] = attribute
    context['entity'] = entity
    context['instance_id'] = instance_id
    context['title'] = title

    return render(request, html_template_path, context)


def create_attr(request,  entity, instance_id, attribute=None):
    html_template_path = 'attrs/create/create-attr.html'
    create_attribute_title = _get_create_attribute_title(attribute)
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
    if attribute == 'shop-link':
        form = ShopLinkForm(request.POST or None)
    if attribute == 'customer-services-link':
        form = CustomerServicesLinkForm(request.POST or None)
    if attribute == 'hall-link':
        form = HallLinkForm(request.POST or None)
    if attribute == 'resource-link':
        form = ResourceLinkForm(request.POST or None)
    if attribute == 'event-location':
        form = EventLocationForm(request.POST or None)
    if attribute in ['place-location', 'school-location', 'organization-location', 'shop-location',
                     'customer-services-location', 'hall-location']:
        if attribute == 'place-location':
            form = CutPlaceLocationForm(request.POST or None)
            form1 = PlaceMapCoordinatesForm(request.POST or None)
        if attribute == 'school-location':
            form = CutSchoolLocationForm(request.POST or None)
            form1 = SchoolMapCoordinatesForm(request.POST or None)
        if attribute == 'organization-location':
            form = CutOrganizationLocationForm(request.POST or None)
            form1 = OrganizationMapCoordinatesForm(request.POST or None)
        if attribute == 'shop-location':
            form = CutShopLocationForm(request.POST or None)
            form1 = ShopMapCoordinatesForm(request.POST or None)
        if attribute == 'customer-services-location':
            form = CutCustomerServicesLocationForm(request.POST or None)
            form1 = CustomerServicesMapCoordinatesForm(request.POST or None)
        if attribute == 'hall-location':
            form = CutHallLocationForm(request.POST or None)
            form1 = HallMapCoordinatesForm(request.POST or None)
        if form.is_valid():
            coordinates = form1.save()
            location = form.save(commit=False)
            location.coordinates = coordinates
            location.save()
            return HttpResponseRedirect('/%s-%s/edit/' % (entity, instance_id))
        context = {
            'form': form,
            'form1': form1,
            'entity': entity,
            'instance_id': instance_id,
            'attribute': attribute,
            'create_attribute_title': create_attribute_title
        }
        return render(request, html_template_path, context)
    if attribute == 'phone-number':
        form = PhoneNumberForm(request.POST or None)
    if attribute == 'chapter-tag':
        form = ChapterTagForm(request.POST or None)
    if attribute == 'album-tag':
        form = AlbumTagForm(request.POST or None)
    if attribute == 'playlist-tag':
        form = PlaylistTagForm(request.POST or None)
    if attribute == 'tracklist-tag':
        form = TracklistTagForm(request.POST or None)
    if attribute == 'dance-direction-tag':
        form = DanceDirectionTagForm(request.POST or None)
    if attribute == 'article-tag':
        form = ArticleTagForm(request.POST or None)
    if attribute == 'photo-tag':
        form = PhotoTagForm(request.POST or None)
    if attribute == 'video-tag':
        form = VideoTagForm(request.POST or None)
    if attribute == 'audio-tag':
        form = AudioTagForm(request.POST or None)
    if attribute == 'dance-style-tag':
        form = DanceStyleTagForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/%s-%s/edit/' % (entity, instance_id))
    context = {
        'form': form,
        'entity': entity,
        'instance_id': instance_id,
        'attribute': attribute,
        'create_attribute_title': create_attribute_title
    }
    return render(request, html_template_path, context)
