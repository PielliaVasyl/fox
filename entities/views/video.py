# -*- coding: utf-8 -*-

from entities.edit_forms.video import EditVideoTitleForm, EditVideoDirectionsForm, EditVideoDescriptionForm, \
    EditVideoTagsForm, EditVideoGroupsForm, EditVideoPolicyForm, EditVideoVideoLinkForm

VIDEO_EDIT_BUTTONS = [
    ('video', 'title', 'Название'),
    ('video', 'directions', 'Направления'),
    ('video', 'description', 'Описание'),
    ('video', 'video-tags', 'Теги'),
    ('video', 'video-link', 'Ссылка'),
    ('video', 'video-groups', 'Плейлист'),
    ('video', 'policy', 'Права пользователей')
]

VIDEO_ATTRIBUTE_FORMS = {
    'title': EditVideoTitleForm,
    'directions': EditVideoDirectionsForm,
    'description': EditVideoDescriptionForm,
    'video-tags': EditVideoTagsForm,
    'video-link': EditVideoVideoLinkForm,
    'video-groups': EditVideoGroupsForm,
    'policy': EditVideoPolicyForm,
}
