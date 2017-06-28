# coding: utf-8

from django import forms

from entities.models.links import AbstractLink, ArticleLink, AudioLink, PhotoLink, PlaylistLink, VideoLink, \
    PlaceLink, SchoolLink, OrganizationLink, TeacherLink, PersonLink, ShopLink, CustomerServicesLink, HallLink, \
    ResourceLink, PromoActionLink, EventLink


class AbstractLinkForm(forms.ModelForm):
    class Meta:
        model = AbstractLink
        fields = ['link', 'author']


# class AbstractEventLinkForm(forms.ModelForm):
#     class Meta:
#         model = AbstractEventLink
#         fields = ['link', 'author']


class EventLinkForm(forms.ModelForm):
    class Meta:
        model = EventLink
        fields = ['link', 'author']


class PromoActionLinkForm(forms.ModelForm):
    class Meta:
        model = PromoActionLink
        fields = ['link', 'author']


# class AbstractPageLinkForm(forms.ModelForm):
#     class Meta:
#         model = AbstractPageLink
#         fields = ['link', 'author']


class PlaceLinkForm(forms.ModelForm):
    class Meta:
        model = PlaceLink
        fields = ['link', 'author']


class SchoolLinkForm(forms.ModelForm):
    class Meta:
        model = SchoolLink
        fields = ['link', 'author']


class OrganizationLinkForm(forms.ModelForm):
    class Meta:
        model = OrganizationLink
        fields = ['link', 'author']


class TeacherLinkForm(forms.ModelForm):
    class Meta:
        model = TeacherLink
        fields = ['link', 'author']


class PersonLinkForm(forms.ModelForm):
    class Meta:
        model = PersonLink
        fields = ['link', 'author']


class ShopLinkForm(forms.ModelForm):
    class Meta:
        model = ShopLink
        fields = ['link', 'author']


class CustomerServicesLinkForm(forms.ModelForm):
    class Meta:
        model = CustomerServicesLink
        fields = ['link', 'author']


class HallLinkForm(forms.ModelForm):
    class Meta:
        model = HallLink
        fields = ['link', 'author']


class ResourceLinkForm(forms.ModelForm):
    class Meta:
        model = ResourceLink
        fields = ['link', 'author']


class PlaylistLinkForm(forms.ModelForm):
    class Meta:
        model = PlaylistLink
        fields = ['link', 'author']


class ArticleLinkForm(forms.ModelForm):
    class Meta:
        model = ArticleLink
        fields = ['link', 'author']


class PhotoLinkForm(forms.ModelForm):
    class Meta:
        model = PhotoLink
        fields = ['link', 'author']


class VideoLinkForm(forms.ModelForm):
    class Meta:
        model = VideoLink
        fields = ['link', 'author']


class AudioLinkForm(forms.ModelForm):
    class Meta:
        model = AudioLink
        fields = ['link', 'author']
