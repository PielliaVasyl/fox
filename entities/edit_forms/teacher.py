from django import forms

from entities.models import Socials
from entities.models import Teacher
from entities.models import TeacherContacts
from entities.models.supportclasses import TeacherLocalClasses


class EditTeacherTitleForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['title']


class EditTeacherDirectionsForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['directions']


class EditTeacherCitiesForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['cities']


class EditTeacherTeacherDanceClassesForm(forms.ModelForm):
    class Meta:
        model = TeacherLocalClasses
        fields = ['dance_styles', 'dance_directions']


class EditTeacherDescriptionForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['description']


class EditTeacherImageForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['image']


class EditTeacherEmployersForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['employers']


class EditTeacherLinksForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['links']


class EditTeacherTeacherContactForm(forms.ModelForm):
    class Meta:
        model = TeacherContacts
        fields = ['phone_numbers']


class EditTeacherSocialsForm(forms.ModelForm):
    class Meta:
        model = Socials
        fields = ['fb', 'vk', 'instagram', 'twitter', 'author']


class EditTeacherPolicyForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['owners', 'contributors', 'author']
