from django import forms

from entities.models.contacts import HallContacts, Socials
from entities.models.pages import Hall


class EditHallTitleForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ['title']


class EditHallDirectionsForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ['directions']


class EditHallCitiesForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ['cities']


class EditHallDescriptionForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ['description']


class EditHallImageForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ['image']


class EditHallHallLocationForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ['locations']


class EditHallEmployeesForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ['employees']


class EditHallLinksForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ['links']


class EditHallHallContactForm(forms.ModelForm):
    class Meta:
        model = HallContacts
        fields = ['phone_numbers']


class EditHallSocialsForm(forms.ModelForm):
    class Meta:
        model = Socials
        fields = ['fb', 'vk', 'instagram', 'twitter', 'author']


class EditHallPolicyForm(forms.ModelForm):
    class Meta:
        model = Hall
        fields = ['owners', 'contributors', 'author']
