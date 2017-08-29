# -*- coding: utf-8 -*-

from entities.edit_forms.album import EditAlbumTitleForm, EditAlbumDirectionsForm, EditAlbumDescriptionForm, \
    EditAlbumTagsForm, EditAlbumPolicyForm

ALBUM_EDIT_BUTTONS = [
    ('album', 'title', 'Название'),
    ('album', 'directions', 'Направления'),
    ('album', 'description', 'Описание'),
    ('album', 'album-tags', 'Теги'),
    ('album', 'policy', 'Права пользователей')
]

ALBUM_ATTRIBUTE_FORMS = {
    'title': EditAlbumTitleForm,
    'directions': EditAlbumDirectionsForm,
    'description': EditAlbumDescriptionForm,
    'album-tags': EditAlbumTagsForm,
    'policy': EditAlbumPolicyForm
}
