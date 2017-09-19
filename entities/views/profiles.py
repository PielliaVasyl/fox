from django.shortcuts import render, get_object_or_404

from entities.edit_forms.profile import EditProfileTitleForm, EditProfileDescriptionForm, EditProfileImageForm
from entities.forms.classes import SelectCityForm, SelectDirectionForm
from entities.models import UserProfile

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


def settings(request, instance_id=None):
    html_template_path = 'entities/profile/profile-settings.html'

    current_instance = get_object_or_404(UserProfile, pk=instance_id)
    title = current_instance.user.username

    select_city_form = SelectCityForm(initial={'city': request.session.get('city_id', 0)})
    select_direction_form = SelectDirectionForm(initial={'direction': request.session.get('direction_id', 0)})

    context = {
        'title': title,
        'instance': current_instance,
        'select_city_form': select_city_form,
        'select_direction_form': select_direction_form
    }
    return render(request, html_template_path, context)
