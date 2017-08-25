from django import forms

from entities.models import Socials
from entities.models.contacts import CustomerServicesContacts
from entities.models.pages import CustomerServices
from entities.models.types import CustomerServicesType


class EditCustomerServicesTitleForm(forms.ModelForm):
    class Meta:
        model = CustomerServices
        fields = ['title']


class EditCustomerServicesDirectionsForm(forms.ModelForm):
    class Meta:
        model = CustomerServices
        fields = ['directions']


class EditCustomerServicesCitiesForm(forms.ModelForm):
    class Meta:
        model = CustomerServices
        fields = ['cities']


class EditCustomerServicesCustomerServicesTypesForm(forms.ModelForm):
    types = forms.MultipleChoiceField(choices=CustomerServicesType.TITLE_CHOICES)


class EditCustomerServicesDescriptionForm(forms.ModelForm):
    class Meta:
        model = CustomerServices
        fields = ['description']


class EditCustomerServicesImageForm(forms.ModelForm):
    class Meta:
        model = CustomerServices
        fields = ['image']


class EditCustomerServicesCustomerServicesLocationForm(forms.ModelForm):
    class Meta:
        model = CustomerServices
        fields = ['locations']


class EditCustomerServicesEmployeesForm(forms.ModelForm):
    class Meta:
        model = CustomerServices
        fields = ['employees']


class EditCustomerServicesLinksForm(forms.ModelForm):
    class Meta:
        model = CustomerServices
        fields = ['links']


class EditCustomerServicesCustomerServicesContactForm(forms.ModelForm):
    class Meta:
        model = CustomerServicesContacts
        fields = ['phone_numbers']


class EditCustomerServicesSocialsForm(forms.ModelForm):
    class Meta:
        model = Socials
        fields = ['fb', 'vk', 'instagram', 'twitter', 'author']


class EditCustomerServicesPolicyForm(forms.ModelForm):
    class Meta:
        model = CustomerServices
        fields = ['owners', 'contributors', 'author']
