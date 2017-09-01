from entities.edit_forms.profile import EditProfileTitleForm, EditProfileDescriptionForm, EditProfileImageForm

PROFILE_EDIT_BUTTONS = [
    ('profile', 'name', 'Имя'),
    ('profile', 'description', 'Описание'),
    ('profile', 'image', 'Фото'),
]

PROFILE_ATTRIBUTE_FORMS = {
    'name': EditProfileTitleForm,
    'description': EditProfileDescriptionForm,
    'image': EditProfileImageForm
}
