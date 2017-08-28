# -*- coding: utf-8 -*-

from entities.edit_forms.article import EditArticleTitleForm, EditArticleDirectionsForm, EditArticleDescriptionForm, \
    EditArticleImageForm, EditArticleTagsForm, EditArticleLinkForm, EditArticleGroupsForm, EditArticlePolicyForm

ARTICLE_EDIT_BUTTONS = [
    ('article', 'title', 'Название'),
    ('article', 'directions', 'Направления'),
    ('article', 'description', 'Текст и автор'),
    ('article', 'image', 'Изображение'),
    ('article', 'article-tags', 'Теги'),
    ('article', 'article-link', 'Ссылка'),
    ('article', 'article-groups', 'Главы'),
    ('article', 'policy', 'Права пользователей')
]

ARTICLE_ATTRIBUTE_FORMS = {
    'title': EditArticleTitleForm,
    'directions': EditArticleDirectionsForm,
    'description': EditArticleDescriptionForm,
    'image': EditArticleImageForm,
    'article-tags': EditArticleTagsForm,
    'article-link': EditArticleLinkForm,
    'article-groups': EditArticleGroupsForm,
    'policy': EditArticlePolicyForm,
}
