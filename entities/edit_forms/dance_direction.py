from django import forms

from entities.models import DanceDirection


class EditDanceDirectionTitleForm(forms.ModelForm):
    class Meta:
        model = DanceDirection
        fields = ['title']


class EditDanceDirectionDescriptionForm(forms.ModelForm):
    class Meta:
        model = DanceDirection
        fields = ['description']


class EditDanceDirectionTagsForm(forms.ModelForm):
    class Meta:
        model = DanceDirection
        fields = ['tags']


class EditDanceDirectionPolicyForm(forms.ModelForm):
    class Meta:
        model = DanceDirection
        fields = ['owners', 'contributors', 'author']
