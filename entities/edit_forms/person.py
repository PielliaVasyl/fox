from django import forms

from entities.models import Socials
from entities.models.contacts import PersonContacts
from entities.models.pages import Person
from entities.models.supportclasses import PersonLocalClasses


class EditPersonTitleForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['title']


class EditPersonDirectionsForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['directions']


class EditPersonCitiesForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['cities']


class EditPersonPersonDanceClassesForm(forms.ModelForm):
    class Meta:
        model = PersonLocalClasses
        fields = ['dance_styles', 'dance_directions']


class EditPersonDescriptionForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['description']


class EditPersonImageForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['image']


class EditPersonEmployersForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['employers']


class EditPersonLinksForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['links']


class EditPersonPersonContactForm(forms.ModelForm):
    class Meta:
        model = PersonContacts
        fields = ['phone_numbers']


class EditPersonSocialsForm(forms.ModelForm):
    class Meta:
        model = Socials
        fields = ['fb', 'vk', 'instagram', 'twitter', 'author']


class EditPersonPolicyForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['owners', 'contributors', 'author']
