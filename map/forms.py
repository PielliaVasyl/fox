from django import forms

from entities.models import Place
from entities.models import School
from entities.models import SchoolContacts
from entities.models import Socials
from entities.models.supportclasses import PlaceLocalClasses, SchoolLocalClasses
from entities.models.types import PlaceType


class EditPlaceTitleForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['title']


class EditPlaceDirectionsForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['directions']


class EditPlaceCitiesForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['cities']


class EditPlaceDescriptionForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['description']


class EditPlaceImageForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['image']


class EditPlacePlaceLocationForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['locations']


class EditPlacePlaceDanceClassesForm(forms.ModelForm):
    class Meta:
        model = PlaceLocalClasses
        fields = ['dance_styles', 'dance_directions']


class EditPlaceTypesForm(forms.Form):
    types = forms.MultipleChoiceField(choices=PlaceType.TITLE_CHOICES)


class EditPlaceLinksForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['links']


class EditPlacePolicyForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['owners', 'contributors', 'author']


# ============================

class EditSchoolTitleForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['title']


class EditSchoolDirectionsForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['directions']


class EditSchoolCitiesForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['cities']


class EditSchoolSchoolDanceClassesForm(forms.ModelForm):
    class Meta:
        model = SchoolLocalClasses
        fields = ['dance_styles', 'dance_directions']


class EditSchoolDescriptionForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['description']


class EditSchoolImageForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['image']


class EditSchoolSchoolLocationForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['locations']


class EditSchoolEmployeesForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['employees']


class EditSchoolLinksForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ['links']


class EditSchoolSchoolContactForm(forms.ModelForm):
    class Meta:
        model = SchoolContacts
        fields = ['phone_numbers']


class EditSchoolSocialsForm(forms.ModelForm):
    class Meta:
        model = Socials
        fields = ['fb', 'vk', 'instagram', 'twitter', 'author']


class EditSchoolPolicyForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['owners', 'contributors', 'author']





