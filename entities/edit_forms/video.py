from django import forms

from entities.models import Video, VideoLink


class EditVideoTitleForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title']


class EditVideoDirectionsForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['directions']


class EditVideoDescriptionForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['description']


class EditVideoTagsForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['tags']


class EditVideoVideoLinkForm(forms.ModelForm):
    class Meta:
        model = VideoLink
        fields = ['link']


class EditVideoGroupsForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['groups']


class EditVideoPolicyForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['owners', 'contributors', 'author']
