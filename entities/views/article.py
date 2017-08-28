# -*- coding: utf-8 -*-

from entities.edit_forms.article import EditArticleTitleForm, EditArticleDirectionsForm, \
    EditArticleDescriptionAndAuthorForm, EditArticleImageForm, EditArticleTagsForm, EditArticleLinkForm, \
    EditArticleGroupsForm, EditArticlePolicyForm

ARTICLE_EDIT_BUTTONS = [
    ('article', 'title', 'Название'),
    ('article', 'directions', 'Направления'),
    ('article', 'description-and-author', 'Текст и автор'),
    ('article', 'image', 'Изображение'),
    ('article', 'article-tags', 'Теги'),
    ('article', 'article-link', 'Ссылка'),
    ('article', 'article-groups', 'Главы'),
    ('article', 'policy', 'Права пользователей')
]

ARTICLE_ATTRIBUTE_FORMS = {
    'title': EditArticleTitleForm,
    'directions': EditArticleDirectionsForm,
    'description-and-author': EditArticleDescriptionAndAuthorForm,
    'image': EditArticleImageForm,
    'article-tags': EditArticleTagsForm,
    'article-link': EditArticleLinkForm,
    'article-groups': EditArticleGroupsForm,
    'policy': EditArticlePolicyForm,
}
