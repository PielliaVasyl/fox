from django import forms
from entities.models.types import EventType, PriceType, ExperienceLevel, RepeatsType, DayOfTheWeek

from entities.models.events import Event


class EditTitleForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title']


class EditDirectionsForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['directions']


class EditCitiesForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['cities']


class EditDescriptionForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['description']


class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['note']


class EditImageForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['image']


class EditVideoForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['video']


class EditDatesForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['start_date', 'end_date']


class EditStatusForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['_status']


class EditEventLocationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['locations']


class EditTypesForm(forms.Form):
    types = forms.MultipleChoiceField(choices=EventType.TITLE_CHOICES)


class EditLinksForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['links']


class EditPriceTypesForm(forms.Form):
    price_types = forms.MultipleChoiceField(choices=PriceType.TITLE_CHOICES)


class EditExperienceLevelsForm(forms.Form):
    experience_levels = forms.MultipleChoiceField(choices=ExperienceLevel.TITLE_CHOICES)


class EditRepeatsTypeForm(forms.Form):
    repeats_type = forms.ChoiceField(choices=RepeatsType.TITLE_CHOICES)


class EditScheduleForm(forms.Form):
    schedule = forms.MultipleChoiceField(choices=DayOfTheWeek.TITLE_CHOICES)


class EditPolicyForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['owners', 'contributors', 'author']
