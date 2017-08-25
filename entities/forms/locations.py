# coding: utf-8

from django import forms

from entities.models import AbstractMapCoordinates, PlaceMapCoordinates, SchoolMapCoordinates, \
    OrganizationMapCoordinates, ShopMapCoordinates, HallMapCoordinates, AbstractLocation, EventLocation, \
    PlaceLocation, SchoolLocation, OrganizationLocation, ShopLocation, HallLocation
from entities.models.locations import CustomerServicesMapCoordinates, CustomerServicesLocation

MAP_COORDINATES_FIELDS = ['lat', 'lng', 'author']
CUT_LOCATION_FIELDS = ['city', 'address', 'note', 'author']
LOCATION_FIELDS = ['city', 'address', 'note', 'coordinates', 'author']


class AbstractMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = AbstractMapCoordinates
        fields = MAP_COORDINATES_FIELDS


class PlaceMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = PlaceMapCoordinates
        fields = MAP_COORDINATES_FIELDS


class SchoolMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = SchoolMapCoordinates
        fields = MAP_COORDINATES_FIELDS


class OrganizationMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = OrganizationMapCoordinates
        fields = MAP_COORDINATES_FIELDS


class ShopMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = ShopMapCoordinates
        fields = MAP_COORDINATES_FIELDS


class CustomerServicesMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = CustomerServicesMapCoordinates
        fields = MAP_COORDINATES_FIELDS


class HallMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = HallMapCoordinates
        fields = MAP_COORDINATES_FIELDS


class AbstractLocationForm(forms.ModelForm):
    class Meta:
        model = AbstractLocation
        fields = CUT_LOCATION_FIELDS


class EventLocationForm(forms.ModelForm):
    class Meta:
        model = EventLocation
        fields = CUT_LOCATION_FIELDS


class PlaceLocationForm(forms.ModelForm):
    class Meta:
        model = PlaceLocation
        fields = LOCATION_FIELDS


class CutPlaceLocationForm(forms.ModelForm):
    class Meta:
        model = PlaceLocation
        fields = CUT_LOCATION_FIELDS


class SchoolLocationForm(forms.ModelForm):
    class Meta:
        model = SchoolLocation
        fields = LOCATION_FIELDS


class CutSchoolLocationForm(forms.ModelForm):
    class Meta:
        model = SchoolLocation
        fields = CUT_LOCATION_FIELDS


class OrganizationLocationForm(forms.ModelForm):
    class Meta:
        model = OrganizationLocation
        fields = LOCATION_FIELDS


class CutOrganizationLocationForm(forms.ModelForm):
    class Meta:
        model = OrganizationLocation
        fields = CUT_LOCATION_FIELDS


class ShopLocationForm(forms.ModelForm):
    class Meta:
        model = ShopLocation
        fields = LOCATION_FIELDS


class CutShopLocationForm(forms.ModelForm):
    class Meta:
        model = ShopLocation
        fields = CUT_LOCATION_FIELDS


class CustomerServicesLocationForm(forms.ModelForm):
    class Meta:
        model = CustomerServicesLocation
        fields = LOCATION_FIELDS


class CutCustomerServicesLocationForm(forms.ModelForm):
    class Meta:
        model = CustomerServicesLocation
        fields = CUT_LOCATION_FIELDS


class HallLocationForm(forms.ModelForm):
    class Meta:
        model = HallLocation
        fields = LOCATION_FIELDS


class CutHallLocationForm(forms.ModelForm):
    class Meta:
        model = HallLocation
        fields = CUT_LOCATION_FIELDS
