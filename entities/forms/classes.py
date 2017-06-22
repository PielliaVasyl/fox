# coding: utf-8

from django import forms

from entities.models import AbstractClass
from entities.models import AbstractGlobalClass
from entities.models import AbstractLocalClass
from entities.models import City
from entities.models import DanceDirectionClass
from entities.models import DanceStyleClass
from entities.models import Direction


class AbstractClassForm(forms.ModelForm):
    class Meta:
        model = AbstractClass
        fields = ['title']


class AbstractGlobalClassForm(forms.ModelForm):
    class Meta:
        model = AbstractGlobalClass
        fields = ['title']


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['title']


class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = ['title']


class AbstractLocalClassForm(forms.ModelForm):
    class Meta:
        model = AbstractLocalClass
        fields = ['title', 'directions']


class DanceDirectionClassForm(forms.ModelForm):
    class Meta:
        model = DanceDirectionClass
        fields = ['title', 'directions']


class DanceStyleClassForm(forms.ModelForm):
    class Meta:
        model = DanceStyleClass
        fields = ['title', 'directions', 'dance_direction']
