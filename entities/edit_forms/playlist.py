from django import forms

from entities.models import Playlist


class EditPlaylistTitleForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['title']


class EditPlaylistDirectionsForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['directions']


class EditPlaylistDescriptionForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['description']


class EditPlaylistTagsForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['tags']


class EditPlaylistLinkForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['link']


class EditPlaylistPolicyForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['owners', 'contributors', 'author']
