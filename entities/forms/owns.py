# coding: utf-8

from django import forms

from entities.models.owns import SchoolOwns, ResourceOwns, HallOwns, CustomerServicesOwns, ShopOwns, \
    PersonOwns, OrganizationOwns, TeacherOwns, PlaceOwns

OWNS_FIELDS = ['events', 'promo_actions', 'articles', 'chapters', 'photos', 'albums', 'videos', 'playlists', 'audios',
               'tracklists']


class PlaceOwnsForm(forms.ModelForm):
    class Meta:
        model = PlaceOwns
        fields = OWNS_FIELDS


class SchoolOwnsForm(forms.ModelForm):
    class Meta:
        model = SchoolOwns
        fields = OWNS_FIELDS


class OrganizationOwnsForm(forms.ModelForm):
    class Meta:
        model = OrganizationOwns
        fields = OWNS_FIELDS


class TeacherOwnsForm(forms.ModelForm):
    class Meta:
        model = TeacherOwns
        fields = OWNS_FIELDS


class PersonOwnsForm(forms.ModelForm):
    class Meta:
        model = PersonOwns
        fields = OWNS_FIELDS


class ShopOwnsForm(forms.ModelForm):
    class Meta:
        model = ShopOwns
        fields = OWNS_FIELDS


class CustomerServicesOwnsForm(forms.ModelForm):
    class Meta:
        model = CustomerServicesOwns
        fields = OWNS_FIELDS


class HallOwnsForm(forms.ModelForm):
    class Meta:
        model = HallOwns
        fields = OWNS_FIELDS


class ResourceOwnsForm(forms.ModelForm):
    class Meta:
        model = ResourceOwns
        fields = OWNS_FIELDS
