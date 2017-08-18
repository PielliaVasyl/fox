from entities.edit_forms.place import EditPlaceDirectionsForm, EditPlaceDescriptionForm, EditPlaceImageForm, \
    EditPlaceTypesForm, EditPlaceTitleForm, EditPlaceCitiesForm, EditPlaceLinksForm, EditPlacePlaceDanceClassesForm, \
    EditPlacePolicyForm, EditPlacePlaceLocationForm


PLACE_EDIT_BUTTONS = [
    ('place', 'title', 'Название'),
    ('place', 'directions', 'Направления'),
    ('place', 'cities', 'Города'),
    ('place', 'types', 'Типы мест'),
    ('place', 'place-dance-classes', 'Танцевальные стили и направления'),
    ('place', 'description', 'Описание'),
    ('place', 'image', 'Изображение'),
    ('place', 'place-locations', 'Места проведения'),
    ('place', 'place-links', 'Ссылки'),
    ('place', 'policy', 'Права пользователей'),
]

PLACE_ATTRIBUTE_FORMS = {
    'title': EditPlaceTitleForm,
    'directions': EditPlaceDirectionsForm,
    'cities': EditPlaceCitiesForm,
    'description': EditPlaceDescriptionForm,
    'image': EditPlaceImageForm,
    'place-locations': EditPlacePlaceLocationForm,
    'place-dance-classes': EditPlacePlaceDanceClassesForm,
    'types': EditPlaceTypesForm,
    'place-links': EditPlaceLinksForm,
    'policy': EditPlacePolicyForm
}
