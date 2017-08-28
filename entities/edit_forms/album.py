from django import forms

from entities.models import Album


class EditAlbumTitleForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title']


class EditAlbumDirectionsForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['directions']


class EditAlbumDescriptionForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['description']


class EditAlbumTagsForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['tags']


class EditAlbumPolicyForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['owners', 'contributors', 'author']
