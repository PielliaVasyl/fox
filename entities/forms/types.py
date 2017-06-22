# coding: utf-8

from django import forms

from entities.models.types import AbstractType, EventType, PriceType, ExperienceLevel, RepeatsType, DayOfTheWeek, \
    ShopType, PlaceType, DanceStyleCountType, DanceStyleDistanceType


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


class CustomerServicesTypeForm(forms.ModelForm):
    class Meta:
        model = ShopType
        fields = ['title', 'description']


class DanceStyleCountTypeForm(forms.ModelForm):
    class Meta:
        model = DanceStyleCountType
        fields = ['title', 'description']


class DanceStyleDistanceTypeForm(forms.ModelForm):
    class Meta:
        model = DanceStyleDistanceType
        fields = ['title', 'description']
