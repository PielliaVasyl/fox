from entities.edit_forms.event import EditEventTitleForm, EditEventDirectionsForm, EditEventCitiesForm, \
    EditEventDescriptionForm, \
    EditEventNoteForm, EditEventImageForm, EditEventVideoForm, EditEventDatesForm, EditEventStatusForm, \
    EditEventTypesForm, EditEventLinksForm, EditEventPriceTypesForm, EditEventExperienceLevelsForm, \
    EditEventRepeatsTypeForm, EditEventScheduleForm, EditEventPolicyForm, EditEventEventLocationForm, \
    EditEventEventDanceClassesForm

EVENT_EDIT_BUTTONS = [
    ('event', 'title', 'Название'),
    ('event', 'directions', 'Направления'),
    ('event', 'cities', 'Города'),
    ('event', 'types', 'Типы мероприятия'),
    ('event', 'event-dance-classes', 'Танцевальные стили и направления'),
    ('event', 'description', 'Описание'),
    ('event', 'note', 'Примечание'),
    ('event', 'image', 'Изображение'),
    ('event', 'video', 'Видео'),
    ('event', 'dates', 'Даты проведения'),
    ('event', 'status', 'Статус'),
    ('event', 'event-locations', 'Места проведения'),
    ('event', 'event-links', 'Ссылки'),
    ('event', 'price-types', 'Типы цен'),
    ('event', 'experience-levels', 'Уровни опыта'),
    ('event', 'repeats-type', 'Частота проведения'),
    ('event', 'schedule', 'Расписание'),
    ('event', 'policy', 'Права пользователей'),
]

EVENT_ATTRIBUTE_FORMS = {
    'title': EditEventTitleForm,
    'directions': EditEventDirectionsForm,
    'cities': EditEventCitiesForm,
    'description': EditEventDescriptionForm,
    'note': EditEventNoteForm,
    'image': EditEventImageForm,
    'video': EditEventVideoForm,
    'dates': EditEventDatesForm,
    'status': EditEventStatusForm,
    'event-locations': EditEventEventLocationForm,
    'event-dance-classes': EditEventEventDanceClassesForm,
    'types': EditEventTypesForm,
    'event-links': EditEventLinksForm,
    'price-types': EditEventPriceTypesForm,
    'experience-levels': EditEventExperienceLevelsForm,
    'repeats-type': EditEventRepeatsTypeForm,
    'schedule': EditEventScheduleForm,
    'policy': EditEventPolicyForm
}