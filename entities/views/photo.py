# -*- coding: utf-8 -*-

from entities.edit_forms.photo import EditPhotoTitleForm, EditPhotoDirectionsForm, EditPhotoDescriptionForm, \
    EditPhotoImageForm, EditPhotoTagsForm, EditPhotoLinkForm, EditPhotoGroupsForm, EditPhotoPolicyForm

PHOTO_EDIT_BUTTONS = [
    ('photo', 'title', 'Название'),
    ('photo', 'directions', 'Направления'),
    ('photo', 'description', 'Описание'),
    ('photo', 'image', 'Изображение'),
    ('photo', 'photo-tags', 'Теги'),
    ('photo', 'photo-link', 'Ссылка'),
    ('photo', 'photo-groups', 'Альбомы'),
    ('photo', 'policy', 'Права пользователей')
]

PHOTO_ATTRIBUTE_FORMS = {
    'title': EditPhotoTitleForm,
    'directions': EditPhotoDirectionsForm,
    'description': EditPhotoDescriptionForm,
    'image': EditPhotoImageForm,
    'photo-tags': EditPhotoTagsForm,
    'photo-link': EditPhotoLinkForm,
    'photo-groups': EditPhotoGroupsForm,
    'policy': EditPhotoPolicyForm,
}
