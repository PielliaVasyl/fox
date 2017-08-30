# coding: utf-8

from django import forms

from entities.models import EventLocalClasses, PageLocalClasses
from entities.models.supportclasses import PromoActionLocalClasses, PlaceLocalClasses, SchoolLocalClasses, \
    OrganizationLocalClasses, TeacherLocalClasses, PersonLocalClasses

LOCAL_CLASSES_FIELDS = ['dance_styles', 'dance_directions']


class EventLocalClassesForm(forms.ModelForm):
    class Meta:
        model = EventLocalClasses
        fields = LOCAL_CLASSES_FIELDS


class PromoActionLocalClassesForm(forms.ModelForm):
    class Meta:
        model = PromoActionLocalClasses
        fields = LOCAL_CLASSES_FIELDS


class PageLocalClassesForm(forms.ModelForm):
    class Meta:
        model = PageLocalClasses
        fields = LOCAL_CLASSES_FIELDS


class PlaceLocalClassesForm(forms.ModelForm):
    class Meta:
        model = PlaceLocalClasses
        fields = LOCAL_CLASSES_FIELDS


class SchoolLocalClassesForm(forms.ModelForm):
    class Meta:
        model = SchoolLocalClasses
        fields = LOCAL_CLASSES_FIELDS


class OrganizationLocalClassesForm(forms.ModelForm):
    class Meta:
        model = OrganizationLocalClasses
        fields = LOCAL_CLASSES_FIELDS


class TeacherLocalClassesForm(forms.ModelForm):
    class Meta:
        model = TeacherLocalClasses
        fields = LOCAL_CLASSES_FIELDS


class PersonLocalClassesForm(forms.ModelForm):
    class Meta:
        model = PersonLocalClasses
        fields = LOCAL_CLASSES_FIELDS
