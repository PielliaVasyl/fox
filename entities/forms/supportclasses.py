# coding: utf-8

from django import forms

from entities.models import EventLocalClasses, PageLocalClasses
from entities.models.supportclasses import PromoActionLocalClasses


class EventLocalClassesForm(forms.ModelForm):
    class Meta:
        model = EventLocalClasses
        fields = ['dance_styles', 'dance_directions']


class PromoActionLocalClassesForm(forms.ModelForm):
    class Meta:
        model = PromoActionLocalClasses
        fields = ['dance_styles', 'dance_directions']


class PageLocalClassesForm(forms.ModelForm):
    class Meta:
        model = PageLocalClasses
        fields = ['dance_styles', 'dance_directions']
