from django import forms

from entities.models import DanceStyle


class EditDanceStyleTitleForm(forms.ModelForm):
    class Meta:
        model = DanceStyle
        fields = ['title']


class EditDanceStyleDirectionsForm(forms.ModelForm):
    class Meta:
        model = DanceStyle
        fields = ['directions']


class EditDanceStyleDescriptionForm(forms.ModelForm):
    class Meta:
        model = DanceStyle
        fields = ['description']


class EditDanceStyleImageForm(forms.ModelForm):
    class Meta:
        model = DanceStyle
        fields = ['image']


class EditDanceStyleTagsForm(forms.ModelForm):
    class Meta:
        model = DanceStyle
        fields = ['tags']


class EditDanceStyleAuthorForm(forms.ModelForm):
    class Meta:
        model = DanceStyle
        fields = ['author_of_post', 'link_to_author']


class EditDanceStyleGroupForm(forms.ModelForm):
    class Meta:
        model = DanceStyle
        fields = ['group']


class EditDanceStyleCountTypesForm(forms.ModelForm):
    class Meta:
        model = DanceStyle
        fields = ['count_types']


class EditDanceStyleDistanceTypesForm(forms.ModelForm):
    class Meta:
        model = DanceStyle
        fields = ['distance_types']


class EditDanceStylePolicyForm(forms.ModelForm):
    class Meta:
        model = DanceStyle
        fields = ['owners', 'contributors', 'author']
