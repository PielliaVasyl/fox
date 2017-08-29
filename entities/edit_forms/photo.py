from django import forms

from entities.models import Photo, PhotoLink


class EditPhotoTitleForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title']


class EditPhotoDirectionsForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['directions']


class EditPhotoDescriptionForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['description']


class EditPhotoImageForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']


class EditPhotoTagsForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['tags']


class EditPhotoPhotoLinkForm(forms.ModelForm):
    class Meta:
        model = PhotoLink
        fields = ['link']


class EditPhotoGroupsForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['groups']


class EditPhotoPolicyForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['owners', 'contributors', 'author']
