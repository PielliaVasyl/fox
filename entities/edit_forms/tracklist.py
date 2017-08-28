from django import forms

from entities.models import Tracklist


class EditTracklistTitleForm(forms.ModelForm):
    class Meta:
        model = Tracklist
        fields = ['title']


class EditTracklistDirectionsForm(forms.ModelForm):
    class Meta:
        model = Tracklist
        fields = ['directions']


class EditTracklistDescriptionForm(forms.ModelForm):
    class Meta:
        model = Tracklist
        fields = ['description']


class EditTracklistTagsForm(forms.ModelForm):
    class Meta:
        model = Tracklist
        fields = ['tags']


class EditTracklistPolicyForm(forms.ModelForm):
    class Meta:
        model = Tracklist
        fields = ['owners', 'contributors', 'author']
