# coding: utf-8

from django import forms

from entities.models import AbstractEventLink
from entities.models import AbstractLink
from entities.models import AbstractLocation
from entities.models import AbstractType
from entities.models import DayOfTheWeek
from entities.models import EventLocalClasses
from entities.models import EventLocation
from entities.models import EventType
from entities.models import ExperienceLevel
from entities.models import PriceType
from entities.models import RepeatsType


class AbstractLinkForm(forms.ModelForm):
    class Meta:
        model = AbstractLink
        fields = ['link', 'author']


class AbstractEventLinkForm(forms.ModelForm):
    class Meta:
        model = AbstractEventLink
        fields = ['link', 'author']


class EventLocalClassesForm(forms.ModelForm):
    class Meta:
        model = EventLocalClasses
        fields = ['dance_styles', 'dance_directions']


class AbstractTypeForm(forms.ModelForm):
    class Meta:
        model = AbstractType
        fields = ['description']


class EventTypeForm(forms.ModelForm):
    class Meta:
        model = EventType
        fields = ['title', 'description']


class PriceTypeForm(forms.ModelForm):
    class Meta:
        model = PriceType
        fields = ['title', 'description']


class ExperienceLevelForm(forms.ModelForm):
    class Meta:
        model = ExperienceLevel
        fields = ['title', 'description']


class RepeatsTypeForm(forms.ModelForm):
    class Meta:
        model = RepeatsType
        fields = ['title', 'description']


class DayOfTheWeekForm(forms.ModelForm):
    class Meta:
        model = DayOfTheWeek
        fields = ['title', 'description']


class AbstractLocationForm(forms.ModelForm):
    class Meta:
        model = AbstractLocation
        fields = ['city', 'address', 'note', 'author']


class EventLocationForm(forms.ModelForm):
    class Meta:
        model = EventLocation
        fields = ['city', 'address', 'note', 'author']
