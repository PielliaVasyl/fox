# -*- coding: utf-8 -*-

from entities.edit_forms.tracklist import EditTracklistTitleForm, EditTracklistDirectionsForm, EditTracklistDescriptionForm, \
    EditTracklistTagsForm, EditTracklistPolicyForm

TRACKLIST_EDIT_BUTTONS = [
    ('tracklist', 'title', 'Название'),
    ('tracklist', 'directions', 'Направления'),
    ('tracklist', 'description', 'Описание'),
    ('tracklist', 'tracklist-tags', 'Теги'),
    ('tracklist', 'policy', 'Права пользователей')
]

TRACKLIST_ATTRIBUTE_FORMS = {
    'title': EditTracklistTitleForm,
    'directions': EditTracklistDirectionsForm,
    'description': EditTracklistDescriptionForm,
    'tracklist-tags': EditTracklistTagsForm,
    'policy': EditTracklistPolicyForm
}
