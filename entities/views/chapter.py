# -*- coding: utf-8 -*-

from entities.edit_forms.chapter import EditChapterTitleForm, EditChapterDirectionsForm, EditChapterDescriptionForm, \
    EditChapterTagsForm, EditChapterPolicyForm

CHAPTER_EDIT_BUTTONS = [
    ('chapter', 'title', 'Название'),
    ('chapter', 'directions', 'Направления'),
    ('chapter', 'description', 'Описание'),
    ('chapter', 'chapter-tags', 'Теги'),
    ('chapter', 'policy', 'Права пользователей')
]

CHAPTER_ATTRIBUTE_FORMS = {
    'title': EditChapterTitleForm,
    'directions': EditChapterDirectionsForm,
    'description': EditChapterDescriptionForm,
    'chapter-tags': EditChapterTagsForm,
    'policy': EditChapterPolicyForm
}
