from django import forms

from entities.models import Socials
from entities.models.contacts import ShopContacts
from entities.models.pages import Shop
from entities.models.types import ShopType


class EditShopTitleForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['title']


class EditShopDirectionsForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['directions']


class EditShopCitiesForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['cities']


class EditShopShopTypesForm(forms.Form):
    types = forms.MultipleChoiceField(choices=ShopType.TITLE_CHOICES)


class EditShopDescriptionForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['description']


class EditShopImageForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['image']


class EditShopShopLocationForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['locations']


class EditShopEmployeesForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['employees']


class EditShopLinksForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['links']


class EditShopShopContactForm(forms.ModelForm):
    class Meta:
        model = ShopContacts
        fields = ['phone_numbers']


class EditShopSocialsForm(forms.ModelForm):
    class Meta:
        model = Socials
        fields = ['fb', 'vk', 'instagram', 'twitter', 'author']


class EditShopPolicyForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['owners', 'contributors', 'author']
