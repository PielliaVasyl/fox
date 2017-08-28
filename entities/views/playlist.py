# -*- coding: utf-8 -*-

from entities.edit_forms.playlist import EditPlaylistTitleForm, EditPlaylistDirectionsForm, EditPlaylistTagsForm, \
    EditPlaylistDescriptionForm, EditPlaylistLinkForm, EditPlaylistPolicyForm

PLAYLIST_EDIT_BUTTONS = [
    ('playlist', 'title', 'Название'),
    ('playlist', 'directions', 'Направления'),
    ('playlist', 'description', 'Описание'),
    ('playlist', 'playlist-tags', 'Теги'),
    ('playlist', 'playlist-link', 'Ссылка'),
    ('playlist', 'policy', 'Права пользователей')
]

PLAYLIST_ATTRIBUTE_FORMS = {
    'title': EditPlaylistTitleForm,
    'directions': EditPlaylistDirectionsForm,
    'description': EditPlaylistDescriptionForm,
    'playlist-tags': EditPlaylistTagsForm,
    'playlist-link': EditPlaylistLinkForm,
    'policy': EditPlaylistPolicyForm
}
