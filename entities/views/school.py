from entities.edit_forms.school import EditSchoolTitleForm, EditSchoolDirectionsForm, \
    EditSchoolSchoolDanceClassesForm, EditSchoolCitiesForm, EditSchoolDescriptionForm, EditSchoolImageForm, \
    EditSchoolSchoolLocationForm, EditSchoolLinksForm, EditSchoolPolicyForm, EditSchoolEmployeesForm, \
    EditSchoolSchoolContactForm, EditSchoolSocialsForm


SCHOOL_EDIT_BUTTONS = [
    ('school', 'title', 'Название'),
    ('school', 'directions', 'Направления'),
    ('school', 'cities', 'Города'),
    ('school', 'school-dance-classes', 'Танцевальные стили и направления'),
    ('school', 'description', 'Описание'),
    ('school', 'image', 'Изображение'),
    ('school', 'school-locations', 'Места'),
    ('school', 'employees', 'Сотрудники'),
    ('school', 'school-links', 'Ссылки'),
    ('school', 'school-contacts', 'Контакты'),
    ('school', 'policy', 'Права пользователей'),
]

SCHOOL_ATTRIBUTE_FORMS = {
    'title': EditSchoolTitleForm,
    'directions': EditSchoolDirectionsForm,
    'cities': EditSchoolCitiesForm,
    'description': EditSchoolDescriptionForm,
    'image': EditSchoolImageForm,
    'school-locations': EditSchoolSchoolLocationForm,
    'school-dance-classes': EditSchoolSchoolDanceClassesForm,
    'school-links': EditSchoolLinksForm,
    'policy': EditSchoolPolicyForm,
    'employees': EditSchoolEmployeesForm,
    'contacts': EditSchoolSchoolContactForm,
    'socials': EditSchoolSocialsForm
}
