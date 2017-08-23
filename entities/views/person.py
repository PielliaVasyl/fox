from entities.edit_forms.person import EditPersonTitleForm, EditPersonDirectionsForm, EditPersonCitiesForm, \
    EditPersonDescriptionForm, EditPersonImageForm, EditPersonPersonDanceClassesForm, EditPersonLinksForm, \
    EditPersonPolicyForm, EditPersonEmployersForm, EditPersonPersonContactForm, EditPersonSocialsForm


PERSON_EDIT_BUTTONS = [
    ('person', 'title', 'Имя'),
    ('person', 'directions', 'Направления'),
    ('person', 'cities', 'Города'),
    ('person', 'person-dance-classes', 'Танцевальные стили и направления'),
    ('person', 'description', 'Описание'),
    ('person', 'employers', 'Работает в'),
    ('person', 'image', 'Фото'),
    ('person', 'person-links', 'Ссылки'),
    ('person', 'person-contacts', 'Контакты'),
    ('person', 'policy', 'Права пользователей'),
]

PERSON_ATTRIBUTE_FORMS = {
    'title': EditPersonTitleForm,
    'directions': EditPersonDirectionsForm,
    'cities': EditPersonCitiesForm,
    'description': EditPersonDescriptionForm,
    'image': EditPersonImageForm,
    'person-dance-classes': EditPersonPersonDanceClassesForm,
    'person-links': EditPersonLinksForm,
    'policy': EditPersonPolicyForm,
    'employers': EditPersonEmployersForm,
    'contacts': EditPersonPersonContactForm,
    'socials': EditPersonSocialsForm
}
