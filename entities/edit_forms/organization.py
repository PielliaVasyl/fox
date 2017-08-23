from django import forms

from entities.models import Organization
from entities.models import OrganizationContacts
from entities.models import Socials
from entities.models.supportclasses import OrganizationLocalClasses


class EditOrganizationTitleForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['title']


class EditOrganizationDirectionsForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['directions']


class EditOrganizationCitiesForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['cities']


class EditOrganizationOrganizationDanceClassesForm(forms.ModelForm):
    class Meta:
        model = OrganizationLocalClasses
        fields = ['dance_styles', 'dance_directions']


class EditOrganizationDescriptionForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['description']


class EditOrganizationImageForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['image']


class EditOrganizationOrganizationLocationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['locations']


class EditOrganizationEmployeesForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['employees']


class EditOrganizationLinksForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['links']


class EditOrganizationOrganizationContactForm(forms.ModelForm):
    class Meta:
        model = OrganizationContacts
        fields = ['phone_numbers']


class EditOrganizationSocialsForm(forms.ModelForm):
    class Meta:
        model = Socials
        fields = ['fb', 'vk', 'instagram', 'twitter', 'author']


class EditOrganizationPolicyForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['owners', 'contributors', 'author']
