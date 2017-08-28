# -*- coding: utf-8 -*-

from entities.edit_forms.audio import EditAudioTitleForm, EditAudioDirectionsForm, EditAudioDescriptionForm, \
    EditAudioTagsForm, EditAudioLinkForm, EditAudioGroupsForm, EditAudioPolicyForm

AUDIO_EDIT_BUTTONS = [
    ('audio', 'title', 'Название'),
    ('audio', 'directions', 'Направления'),
    ('audio', 'description', 'Описание'),
    ('audio', 'audio-tags', 'Теги'),
    ('audio', 'audio-link', 'Ссылка'),
    ('audio', 'audio-groups', 'Плейлист'),
    ('audio', 'policy', 'Права пользователей')
]

AUDIO_ATTRIBUTE_FORMS = {
    'title': EditAudioTitleForm,
    'directions': EditAudioDirectionsForm,
    'description': EditAudioDescriptionForm,
    'audio-tags': EditAudioTagsForm,
    'audio-link': EditAudioLinkForm,
    'audio-groups': EditAudioGroupsForm,
    'policy': EditAudioPolicyForm,
}
