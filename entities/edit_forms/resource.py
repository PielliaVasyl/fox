from django import forms

from entities.models import ResourceContacts, Resource
from entities.models import Socials


class EditResourceTitleForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title']


class EditResourceDirectionsForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['directions']


class EditResourceCitiesForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['cities']


class EditResourceDescriptionForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['description']


class EditResourceImageForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['image']


class EditResourceEmployeesForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['employees']


class EditResourceLinksForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['links']


class EditResourceResourceContactForm(forms.ModelForm):
    class Meta:
        model = ResourceContacts
        fields = ['phone_numbers']


class EditResourceSocialsForm(forms.ModelForm):
    class Meta:
        model = Socials
        fields = ['fb', 'vk', 'instagram', 'twitter', 'author']


class EditResourcePolicyForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['owners', 'contributors', 'author']
