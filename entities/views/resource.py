from entities.edit_forms.resource import EditResourceTitleForm, EditResourceDirectionsForm, EditResourceCitiesForm, \
    EditResourceDescriptionForm, EditResourceImageForm, EditResourceLinksForm, EditResourcePolicyForm, \
    EditResourceResourceContactForm, EditResourceSocialsForm, EditResourceEmployeesForm

RESOURCE_EDIT_BUTTONS = [
    ('resource', 'title', 'Название'),
    ('resource', 'directions', 'Направления'),
    ('resource', 'cities', 'Города'),
    ('resource', 'description', 'Описание'),
    ('resource', 'image', 'Изображение'),
    ('resource', 'employees', 'Сотрудники'),
    ('resource', 'resource-links', 'Ссылки'),
    ('resource', 'resource-contacts', 'Контакты'),
    ('resource', 'policy', 'Права пользователей'),
]

RESOURCE_ATTRIBUTE_FORMS = {
    'title': EditResourceTitleForm,
    'directions': EditResourceDirectionsForm,
    'cities': EditResourceCitiesForm,
    'description': EditResourceDescriptionForm,
    'image': EditResourceImageForm,
    'resource-links': EditResourceLinksForm,
    'policy': EditResourcePolicyForm,
    'employees': EditResourceEmployeesForm,
    'contacts': EditResourceResourceContactForm,
    'socials': EditResourceSocialsForm
}
