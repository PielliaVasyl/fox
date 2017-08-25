from entities.edit_forms.hall import EditHallTitleForm, EditHallDirectionsForm, EditHallCitiesForm, \
    EditHallDescriptionForm, EditHallImageForm, EditHallHallLocationForm, EditHallLinksForm, EditHallPolicyForm, \
    EditHallEmployeesForm, EditHallHallContactForm, EditHallSocialsForm

HALL_EDIT_BUTTONS = [
    ('hall', 'title', 'Название'),
    ('hall', 'directions', 'Направления'),
    ('hall', 'cities', 'Города'),
    ('hall', 'description', 'Описание'),
    ('hall', 'image', 'Изображение'),
    ('hall', 'hall-locations', 'Места'),
    ('hall', 'employees', 'Сотрудники'),
    ('hall', 'hall-links', 'Ссылки'),
    ('hall', 'hall-contacts', 'Контакты'),
    ('hall', 'policy', 'Права пользователей'),
]

HALL_ATTRIBUTE_FORMS = {
    'title': EditHallTitleForm,
    'directions': EditHallDirectionsForm,
    'cities': EditHallCitiesForm,
    'description': EditHallDescriptionForm,
    'image': EditHallImageForm,
    'hall-locations': EditHallHallLocationForm,
    'hall-links': EditHallLinksForm,
    'policy': EditHallPolicyForm,
    'employees': EditHallEmployeesForm,
    'contacts': EditHallHallContactForm,
    'socials': EditHallSocialsForm
}
