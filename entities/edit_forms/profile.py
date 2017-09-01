from django import forms
from django.contrib.auth.models import User

from entities.models import UserProfile


class EditProfileTitleForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']


class EditProfileDescriptionForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['description']


class EditProfileImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']
