from django import forms

from entities.models import Playlist, PlaylistLink


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


class EditPlaylistPlaylistLinkForm(forms.ModelForm):
    class Meta:
        model = PlaylistLink
        fields = ['link']


class EditPlaylistPolicyForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['owners', 'contributors', 'author']
