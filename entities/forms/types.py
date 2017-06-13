# coding: utf-8

from django import forms

from entities.models import AbstractType, EventType, PriceType, ExperienceLevel, RepeatsType, DayOfTheWeek, \
    ShopType, PlaceType


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


class PlaceTypeForm(forms.ModelForm):
    class Meta:
        model = PlaceType
        fields = ['title', 'description']


class ShopTypeForm(forms.ModelForm):
    class Meta:
        model = ShopType
        fields = ['title', 'description']
