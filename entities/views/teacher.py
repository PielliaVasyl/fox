from entities.edit_forms.teacher import EditTeacherTitleForm, EditTeacherDirectionsForm, EditTeacherCitiesForm, \
    EditTeacherDescriptionForm, EditTeacherTeacherDanceClassesForm, EditTeacherEmployersForm, EditTeacherImageForm, \
    EditTeacherLinksForm, EditTeacherPolicyForm, EditTeacherTeacherContactForm, EditTeacherSocialsForm


TEACHER_EDIT_BUTTONS = [
    ('teacher', 'title', 'Имя'),
    ('teacher', 'directions', 'Направления'),
    ('teacher', 'cities', 'Города'),
    ('teacher', 'teacher-dance-classes', 'Танцевальные стили и направления'),
    ('teacher', 'description', 'Описание'),
    ('teacher', 'employers', 'Работает в'),
    ('teacher', 'image', 'Фото'),
    ('teacher', 'teacher-links', 'Ссылки'),
    ('teacher', 'teacher-contacts', 'Контакты'),
    ('teacher', 'policy', 'Права пользователей'),
]

TEACHER_ATTRIBUTE_FORMS = {
    'title': EditTeacherTitleForm,
    'directions': EditTeacherDirectionsForm,
    'cities': EditTeacherCitiesForm,
    'description': EditTeacherDescriptionForm,
    'image': EditTeacherImageForm,
    'teacher-dance-classes': EditTeacherTeacherDanceClassesForm,
    'teacher-links': EditTeacherLinksForm,
    'policy': EditTeacherPolicyForm,
    'employers': EditTeacherEmployersForm,
    'contacts': EditTeacherTeacherContactForm,
    'socials': EditTeacherSocialsForm
}
