from entities.edit_forms.organization import EditOrganizationTitleForm, EditOrganizationDirectionsForm, \
    EditOrganizationCitiesForm, EditOrganizationDescriptionForm, EditOrganizationImageForm, \
    EditOrganizationOrganizationLocationForm, EditOrganizationOrganizationDanceClassesForm, EditOrganizationLinksForm, \
    EditOrganizationPolicyForm, EditOrganizationEmployeesForm, EditOrganizationOrganizationContactForm, \
    EditOrganizationSocialsForm

ORGANIZATION_EDIT_BUTTONS = [
    ('organization', 'title', 'Название'),
    ('organization', 'directions', 'Направления'),
    ('organization', 'cities', 'Города'),
    ('organization', 'organization-dance-classes', 'Танцевальные стили и направления'),
    ('organization', 'description', 'Описание'),
    ('organization', 'image', 'Изображение'),
    ('organization', 'organization-locations', 'Места'),
    ('organization', 'employees', 'Сотрудники'),
    ('organization', 'organization-links', 'Ссылки'),
    ('organization', 'organization-contacts', 'Контакты'),
    ('organization', 'policy', 'Права пользователей'),
]

ORGANIZATION_ATTRIBUTE_FORMS = {
    'title': EditOrganizationTitleForm,
    'directions': EditOrganizationDirectionsForm,
    'cities': EditOrganizationCitiesForm,
    'description': EditOrganizationDescriptionForm,
    'image': EditOrganizationImageForm,
    'organization-locations': EditOrganizationOrganizationLocationForm,
    'organization-dance-classes': EditOrganizationOrganizationDanceClassesForm,
    'organization-links': EditOrganizationLinksForm,
    'policy': EditOrganizationPolicyForm,
    'employees': EditOrganizationEmployeesForm,
    'contacts': EditOrganizationOrganizationContactForm,
    'socials': EditOrganizationSocialsForm
}
