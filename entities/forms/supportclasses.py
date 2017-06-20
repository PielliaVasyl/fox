# coding: utf-8

from django import forms

from entities.models import EventLocalClasses, PageLocalClasses


class EventLocalClassesForm(forms.ModelForm):
    class Meta:
        model = EventLocalClasses
        fields = ['dance_styles', 'dance_directions']


class PageLocalClassesForm(forms.ModelForm):
    class Meta:
        model = PageLocalClasses
        fields = ['dance_styles', 'dance_directions']
