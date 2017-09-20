# coding: utf-8

from django import forms

from entities.models.userprofile import UserSettings


class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = ['city', 'direction']
