from django import forms

from entities.models import Audio, AudioLink


class EditAudioTitleForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['title']


class EditAudioDirectionsForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['directions']


class EditAudioDescriptionForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['description']


class EditAudioTagsForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['tags']


class EditAudioAudioLinkForm(forms.ModelForm):
    class Meta:
        model = AudioLink
        fields = ['link']


class EditAudioGroupsForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['groups']


class EditAudioPolicyForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['owners', 'contributors', 'author']
