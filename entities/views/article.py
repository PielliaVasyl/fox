# -*- coding: utf-8 -*-

from entities.edit_forms.article import EditArticleTitleForm, EditArticleDirectionsForm, \
    EditArticleArticleDescriptionForm, EditArticleImageForm, EditArticleTagsForm, EditArticleArticleLinkForm, \
    EditArticleGroupsForm, EditArticlePolicyForm, EditArticleLinkedForm

ARTICLE_EDIT_BUTTONS = [
    ('article', 'title', 'Название'),
    ('article', 'directions', 'Направления'),
    ('article', 'article-description', 'Текст и автор'),
    ('article', 'image', 'Изображение'),
    ('article', 'article-tags', 'Теги'),
    ('article', 'article-link', 'Ссылка'),
    ('article', 'article-linked', 'Тип статьи'),
    ('article', 'article-groups', 'Главы'),
    ('article', 'policy', 'Права пользователей')
]

ARTICLE_ATTRIBUTE_FORMS = {
    'title': EditArticleTitleForm,
    'directions': EditArticleDirectionsForm,
    'article-description': EditArticleArticleDescriptionForm,
    'image': EditArticleImageForm,
    'article-tags': EditArticleTagsForm,
    'article-link': EditArticleArticleLinkForm,
    'article-linked': EditArticleLinkedForm,
    'article-groups': EditArticleGroupsForm,
    'policy': EditArticlePolicyForm,
}
