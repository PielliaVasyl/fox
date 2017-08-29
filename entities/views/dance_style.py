# -*- coding: utf-8 -*-

from entities.edit_forms.dance_style import EditDanceStyleTitleForm, EditDanceStyleDescriptionForm, \
    EditDanceStyleImageForm, EditDanceStyleTagsForm, EditDanceStyleGroupForm, EditDanceStyleCountTypesForm, \
    EditDanceStyleDistanceTypesForm, EditDanceStylePolicyForm, EditDanceStyleAuthorLink

DANCE_STYLE_EDIT_BUTTONS = [
    ('dance-style', 'title', 'Название'),
    ('dance-style', 'dance-style-description', 'Описание стиля и автор'),
    ('dance-style', 'image', 'Изображение'),
    ('dance-style', 'dance-style-tags', 'Теги'),
    ('dance-style', 'dance-style-group', 'Танцевальное направление'),
    ('dance-style', 'dance-style-count-types', 'Тип по количеству'),
    ('dance-style', 'dance-style-distance-types', 'Расстояние между партнерами'),
    ('dance-style', 'policy', 'Права пользователей')
]

DANCE_STYLE_ATTRIBUTE_FORMS = {
    'title': EditDanceStyleTitleForm,
    'dance-style-description': EditDanceStyleDescriptionForm,
    'dance-style-link': EditDanceStyleAuthorLink,
    'image': EditDanceStyleImageForm,
    'dance-style-tags': EditDanceStyleTagsForm,
    'dance-style-group': EditDanceStyleGroupForm,
    'dance-style-count-types': EditDanceStyleCountTypesForm,
    'dance-style-distance-types': EditDanceStyleDistanceTypesForm,
    'policy': EditDanceStylePolicyForm,
}
