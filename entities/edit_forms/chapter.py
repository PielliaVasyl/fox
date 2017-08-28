from django import forms

from entities.models import Chapter


class EditChapterTitleForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['title']


class EditChapterDirectionsForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['directions']


class EditChapterDescriptionForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['description']


class EditChapterTagsForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['tags']


class EditChapterPolicyForm(forms.ModelForm):
    class Meta:
        model = Chapter
        fields = ['owners', 'contributors', 'author']
