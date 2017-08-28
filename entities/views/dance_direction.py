# -*- coding: utf-8 -*-

from entities.edit_forms.dance_direction import EditDanceDirectionTitleForm, EditDanceDirectionDirectionsForm, \
    EditDanceDirectionDescriptionForm, EditDanceDirectionTagsForm, EditDanceDirectionPolicyForm

DANCE_DIRECTION_EDIT_BUTTONS = [
    ('dance-direction', 'title', 'Название'),
    ('dance-direction', 'directions', 'Направления'),
    ('dance-direction', 'description', 'Описание'),
    ('dance-direction', 'dance-direction-tags', 'Теги'),
    ('dance-direction', 'policy', 'Права пользователей')
]

DANCE_DIRECTION_ATTRIBUTE_FORMS = {
    'title': EditDanceDirectionTitleForm,
    'directions': EditDanceDirectionDirectionsForm,
    'description': EditDanceDirectionDescriptionForm,
    'chapter-tags': EditDanceDirectionTagsForm,
    'policy': EditDanceDirectionPolicyForm
}
