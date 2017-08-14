# coding: utf-8

from django import forms

from entities.models import EventLocalClasses, PageLocalClasses
from entities.models.supportclasses import PromoActionLocalClasses, PlaceLocalClasses, SchoolLocalClasses, \
    OrganizationLocalClasses, TeacherLocalClasses, PersonLocalClasses


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


class PlaceLocalClassesForm(forms.ModelForm):
    class Meta:
        model = PlaceLocalClasses
        fields = ['dance_styles', 'dance_directions']


class SchoolLocalClassesForm(forms.ModelForm):
    class Meta:
        model = SchoolLocalClasses
        fields = ['dance_styles', 'dance_directions']


class OrganizationLocalClassesForm(forms.ModelForm):
    class Meta:
        model = OrganizationLocalClasses
        fields = ['dance_styles', 'dance_directions']


class TeacherLocalClassesForm(forms.ModelForm):
    class Meta:
        model = TeacherLocalClasses
        fields = ['dance_styles', 'dance_directions']


class PersonLocalClassesForm(forms.ModelForm):
    class Meta:
        model = PersonLocalClasses
        fields = ['dance_styles', 'dance_directions']
