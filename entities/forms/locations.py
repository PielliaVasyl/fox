# coding: utf-8

from django import forms

from entities.models import AbstractMapCoordinates, PlaceMapCoordinates, SchoolMapCoordinates, \
    OrganizationMapCoordinates, ShopMapCoordinates, HallMapCoordinates, AbstractLocation, EventLocation, \
    PlaceLocation, SchoolLocation, OrganizationLocation, ShopLocation, HallLocation


class AbstractMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = AbstractMapCoordinates
        fields = ['lat', 'lng', 'author']


class PlaceMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = PlaceMapCoordinates
        fields = ['lat', 'lng', 'author']


class SchoolMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = SchoolMapCoordinates
        fields = ['lat', 'lng', 'author']


class OrganizationMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = OrganizationMapCoordinates
        fields = ['lat', 'lng', 'author']


class ShopMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = ShopMapCoordinates
        fields = ['lat', 'lng', 'author']


class HallMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = HallMapCoordinates
        fields = ['lat', 'lng', 'author']


class AbstractLocationForm(forms.ModelForm):
    class Meta:
        model = AbstractLocation
        fields = ['city', 'address', 'note', 'author']


class EventLocationForm(forms.ModelForm):
    class Meta:
        model = EventLocation
        fields = ['city', 'address', 'note', 'author']


class PlaceLocationForm(forms.ModelForm):
    class Meta:
        model = PlaceLocation
        fields = ['city', 'address', 'note', 'coordinates', 'author']


class SchoolLocationForm(forms.ModelForm):
    class Meta:
        model = SchoolLocation
        fields = ['city', 'address', 'note', 'coordinates', 'author']


class OrganizationLocationForm(forms.ModelForm):
    class Meta:
        model = OrganizationLocation
        fields = ['city', 'address', 'note', 'coordinates', 'author']


class ShopLocationForm(forms.ModelForm):
    class Meta:
        model = ShopLocation
        fields = ['city', 'address', 'note', 'coordinates', 'author']


class HallLocationForm(forms.ModelForm):
    class Meta:
        model = HallLocation
        fields = ['city', 'address', 'note', 'coordinates', 'author']
