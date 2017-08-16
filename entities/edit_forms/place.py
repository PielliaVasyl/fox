from django import forms

from entities.models import Place
from entities.models.supportclasses import PlaceLocalClasses
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
