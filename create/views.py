# -*- coding: utf-8 -*-

from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from entities.forms.events import CutEventForm, CutPromoActionForm
from entities.forms.pages import CutPlaceForm, CutSchoolForm, CutTeacherForm, CutOrganizationForm, CutPersonForm, \
    CutShopForm, CutCustomerServicesForm, CutHallForm, CutResourceForm
from entities.forms.posts import CutArticleForm, CutChapterForm, CutPhotoForm, CutAlbumForm, CutVideoForm, \
    CutPlaylistForm, CutAudioForm, CutTracklistForm, CutDanceStyleForm, CutDanceDirectionForm


def show_create_page(request):
    context = {
    }
    return render(request, 'create/create.html', context)


def create_instance(request, instance=None):
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
        return HttpResponseRedirect('/%s-%s/edit/' % (instance, my_instance.pk))
    context = {
        'form': form,
        'title': title,
        'entity_url': entity_url
    }
    return render(request, html_template_path, context)
