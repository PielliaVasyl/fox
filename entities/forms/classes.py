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


class SelectCityForm(forms.Form):
    city = forms.ChoiceField(label="", widget=forms.Select(attrs={'onChange': 'city_direction.submit();'}))

    def __init__(self, *args, **kwargs):
        cities = City.objects.all()
        city_choices = ((city.id, city.title) for city in cities)
        super(SelectCityForm, self).__init__(*args, **kwargs)
        self.fields['city'].choices = city_choices


class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = ['title']


class SelectDirectionForm(forms.Form):
    direction = forms.ChoiceField(label="", widget=forms.Select(attrs={'onChange': 'city_direction.submit();'}))

    def __init__(self, *args, **kwargs):
        directions = Direction.objects.all()
        direction_choices = ((direction.id, direction.title) for direction in directions)
        super(SelectDirectionForm, self).__init__(*args, **kwargs)
        self.fields['direction'].choices = direction_choices


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
