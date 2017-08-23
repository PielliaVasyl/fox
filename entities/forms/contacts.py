# coding: utf-8

from django import forms

from entities.models import AbstractSocialLink, SocialLinkFB, SocialLinkVK, SocialLinkInstagram, SocialLinkTwitter, \
    Socials, PhoneNumber, AbstractContacts, SchoolContacts, OrganizationContacts, TeacherContacts, PersonContacts, \
    ShopContacts, HallContacts, ResourceContacts
from entities.models.contacts import CustomerServicesContacts


class AbstractSocialLinkForm(forms.ModelForm):
    class Meta:
        model = AbstractSocialLink
        fields = ['link', 'author']


class SocialLinkFBForm(forms.ModelForm):
    class Meta:
        model = SocialLinkFB
        fields = ['link', 'author']


class SocialLinkVKForm(forms.ModelForm):
    class Meta:
        model = SocialLinkVK
        fields = ['link', 'author']


class SocialLinkInstagramForm(forms.ModelForm):
    class Meta:
        model = SocialLinkInstagram
        fields = ['link', 'author']


class SocialLinkTwitterForm(forms.ModelForm):
    class Meta:
        model = SocialLinkTwitter
        fields = ['link', 'author']


class SocialsForm(forms.ModelForm):
    class Meta:
        model = Socials
        fields = ['fb', 'vk', 'instagram', 'twitter', 'author']


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['phone_number', 'author']


class AbstractContactsForm(forms.ModelForm):
    class Meta:
        model = AbstractContacts
        fields = ['phone_numbers', 'socials', 'author']


class SchoolContactsForm(forms.ModelForm):
    class Meta:
        model = SchoolContacts
        fields = ['phone_numbers', 'socials', 'author']


class OrganizationContactsForm(forms.ModelForm):
    class Meta:
        model = OrganizationContacts
        fields = ['phone_numbers', 'socials', 'author']


class TeacherContactsForm(forms.ModelForm):
    class Meta:
        model = TeacherContacts
        fields = ['phone_numbers', 'socials', 'author']


class PersonContactsForm(forms.ModelForm):
    class Meta:
        model = PersonContacts
        fields = ['phone_numbers', 'socials', 'author']


class ShopContactsForm(forms.ModelForm):
    class Meta:
        model = ShopContacts
        fields = ['phone_numbers', 'socials', 'author']


class CustomerServicesContactsForm(forms.ModelForm):
    class Meta:
        model = CustomerServicesContacts
        fields = ['phone_numbers', 'socials', 'author']


class HallContactsForm(forms.ModelForm):
    class Meta:
        model = HallContacts
        fields = ['phone_numbers', 'socials', 'author']


class ResourceContactsForm(forms.ModelForm):
    class Meta:
        model = ResourceContacts
        fields = ['phone_numbers', 'socials', 'author']
