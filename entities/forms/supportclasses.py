# coding: utf-8

from django import forms

from entities.models import AbstractEventLink
from entities.models import AbstractLink
from entities.models import EventLocalClasses
from entities.models import AbstractPageLink, PageLocalClasses


class AbstractLinkForm(forms.ModelForm):
    class Meta:
        model = AbstractLink
        fields = ['link', 'author']


class AbstractEventLinkForm(forms.ModelForm):
    class Meta:
        model = AbstractEventLink
        fields = ['link', 'author']


class AbstractPageLinkForm(forms.ModelForm):
    class Meta:
        model = AbstractPageLink
        fields = ['link', 'author']


class EventLocalClassesForm(forms.ModelForm):
    class Meta:
        model = EventLocalClasses
        fields = ['dance_styles', 'dance_directions']


class PageLocalClassesForm(forms.ModelForm):
    class Meta:
        model = PageLocalClasses
        fields = ['dance_styles', 'dance_directions']
