from entities.edit_forms.promo_action import EditPromoActionTitleForm, EditPromoActionDirectionsForm, \
    EditPromoActionCitiesForm, EditPromoActionDescriptionForm, EditPromoActionNoteForm, EditPromoActionImageForm, \
    EditPromoActionVideoForm, EditPromoActionDatesForm, EditPromoActionStatusForm, \
    EditPromoActionPromoActionDanceClassesForm, EditPromoActionLinksForm, EditPromoActionPolicyForm


PROMO_ACTION_EDIT_BUTTONS = [
    ('promo-action', 'title', 'Название'),
    ('promo-action', 'directions', 'Направления'),
    ('promo-action', 'cities', 'Города'),
    ('promo-action', 'promo-action-dance-classes', 'Танцевальные стили и направления'),
    ('promo-action', 'description', 'Описание'),
    ('promo-action', 'note', 'Примечание'),
    ('promo-action', 'image', 'Изображение'),
    ('promo-action', 'video', 'Видео'),
    ('promo-action', 'dates', 'Даты проведения'),
    ('promo-action', 'status', 'Статус'),
    ('promo-action', 'promo-action-links', 'Ссылки'),
    ('promo-action', 'policy', 'Права пользователей'),
]

PROMO_ACTION_ATTRIBUTE_FORMS = {
    'title': EditPromoActionTitleForm,
    'directions': EditPromoActionDirectionsForm,
    'cities': EditPromoActionCitiesForm,
    'description': EditPromoActionDescriptionForm,
    'note': EditPromoActionNoteForm,
    'image': EditPromoActionImageForm,
    'video': EditPromoActionVideoForm,
    'dates': EditPromoActionDatesForm,
    'status': EditPromoActionStatusForm,
    'promo-action-dance-classes': EditPromoActionPromoActionDanceClassesForm,
    'promo-action-links': EditPromoActionLinksForm,
    'policy': EditPromoActionPolicyForm
}
