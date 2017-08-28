# -*- coding: utf-8 -*-

from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from algoritms.get_direction_city_parameter import get_direction_city_parameter
from entities.forms import EventLocationForm, ArticleTagForm, ChapterTagForm, AlbumTagForm, PlaylistTagForm, \
    TracklistTagForm, DanceDirectionTagForm, PhotoTagForm, VideoTagForm, AudioTagForm, DanceStyleTagForm
from entities.forms import PhoneNumberForm
from entities.forms.classes import DirectionForm, CityForm
from entities.forms.events import CutEventForm, CutPromoActionForm
from entities.forms.links import EventLinkForm, PromoActionLinkForm, PlaceLinkForm, SchoolLinkForm, TeacherLinkForm, \
    ShopLinkForm, CustomerServicesLinkForm, HallLinkForm, OrganizationLinkForm, PersonLinkForm, ResourceLinkForm
from entities.forms.locations import CutPlaceLocationForm, PlaceMapCoordinatesForm, SchoolMapCoordinatesForm, \
    CutSchoolLocationForm, OrganizationMapCoordinatesForm, CutOrganizationLocationForm, ShopMapCoordinatesForm, \
    CutShopLocationForm, CutHallLocationForm, HallMapCoordinatesForm, CutCustomerServicesLocationForm, \
    CustomerServicesMapCoordinatesForm
from entities.forms.pages import CutPlaceForm, CutSchoolForm, CutTeacherForm, CutOrganizationForm, CutPersonForm, \
    CutShopForm, CutCustomerServicesForm, CutHallForm, CutResourceForm
from entities.forms.posts import CutArticleForm, CutChapterForm, CutPhotoForm, CutAlbumForm, CutVideoForm, \
    CutPlaylistForm, CutAudioForm, CutTracklistForm, CutDanceStyleForm, CutDanceDirectionForm


def create(request, city_title=None, direction_title=None):
    context = {
    }
    return render(request, 'create/create.html', context)


def create_instance(request, instance=None, city_title=None, direction_title=None):
    html_template_path = 'create/create-entity.html'
    entity_url = instance
    entity_title = {
        'event': 'мероприятие',
        'promo-action': 'акцию',
        'place': 'место на карте',
        'school': 'школу',
        'teacher': 'учителя',
        'organization': 'организацию',
        'person': 'персону',
        'shop': 'магазин',
        'customer-services': 'услуги',
        'hall': 'зал для оренды',
        'resource': 'информационный ресурс',
        'article': 'статью',
        'chapter': 'главу',
        'photo': 'фото',
        'album': 'Альбом',
        'video': 'Видео',
        'playlist': 'Плейлист',
        'audio': 'Аудио',
        'tracklist': 'треклист',
        'dance-style': 'танцевальный стиль',
        'dance-direction': 'танцевальное направление',
    }.get(instance, 'Неизнестный экземпляр')
    title = 'Добавить ' + entity_title
    form = {
        'event': CutEventForm(request.POST or None),
        'promo-action': CutPromoActionForm(request.POST or None),
        'place': CutPlaceForm(request.POST or None),
        'school': CutSchoolForm(request.POST or None),
        'teacher': CutTeacherForm(request.POST or None),
        'organization': CutOrganizationForm(request.POST or None),
        'person': CutPersonForm(request.POST or None),
        'shop': CutShopForm(request.POST or None),
        'customer-services': CutCustomerServicesForm(request.POST or None),
        'hall': CutHallForm(request.POST or None),
        'resource': CutResourceForm(request.POST or None),
        'article': CutArticleForm(request.POST or None),
        'chapter': CutChapterForm(request.POST or None),
        'photo': CutPhotoForm(request.POST or None),
        'album': CutAlbumForm(request.POST or None),
        'video': CutVideoForm(request.POST or None),
        'playlist': CutPlaylistForm(request.POST or None),
        'audio': CutAudioForm(request.POST or None),
        'tracklist': CutTracklistForm(request.POST or None),
        'dance-style': CutDanceStyleForm(request.POST or None),
        'dance-direction': CutDanceDirectionForm(request.POST or None)
    }.get(instance, None)

    if form.is_valid():
        my_instance = form.save()
        return HttpResponseRedirect('/' + instance + '-%s/edit/%s' %
                                    (my_instance.pk, get_direction_city_parameter(city_title, direction_title)))
    context = {
        'form': form,
        'title': title,
        'entity_url': entity_url
    }
    return render(request, html_template_path, context)


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
        return HttpResponseRedirect('/%s/edit/%s' %
                                    (request.GET.get('instance'),
                                     get_direction_city_parameter(city_title, direction_title)
                                     ))
    context = {
        'form': form,
        'incoming_instance': request.GET.get('instance')

    }
    return render(request, html_template_path, context)
