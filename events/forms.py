from django import forms

from entities.models import EventLocalClasses
from entities.models.types import EventType, PriceType, ExperienceLevel, RepeatsType, DayOfTheWeek

from entities.models.events import Event, PromoAction


class EditEventTitleForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title']


class EditEventDirectionsForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['directions']


class EditEventCitiesForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['cities']


class EditEventDescriptionForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['description']


class EditEventNoteForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['note']


class EditEventImageForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['image']


class EditEventVideoForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['video']


class EditEventDatesForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['start_date', 'end_date']


class EditEventStatusForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['_status']


class EditEventEventLocationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['locations']


class EditEventEventDanceClassesForm(forms.ModelForm):
    class Meta:
        model = EventLocalClasses
        fields = ['dance_styles', 'dance_directions']


class EditEventTypesForm(forms.Form):
    types = forms.MultipleChoiceField(choices=EventType.TITLE_CHOICES)


class EditEventLinksForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['links']


class EditEventPriceTypesForm(forms.Form):
    price_types = forms.MultipleChoiceField(choices=PriceType.TITLE_CHOICES)


class EditEventExperienceLevelsForm(forms.Form):
    experience_levels = forms.MultipleChoiceField(choices=ExperienceLevel.TITLE_CHOICES)


class EditEventRepeatsTypeForm(forms.Form):
    repeats_type = forms.ChoiceField(choices=RepeatsType.TITLE_CHOICES)


class EditEventScheduleForm(forms.Form):
    schedule = forms.MultipleChoiceField(choices=DayOfTheWeek.TITLE_CHOICES)


class EditEventPolicyForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['owners', 'contributors', 'author']


# ============================


class EditPromoActionTitleForm(forms.ModelForm):
    class Meta:
        model = PromoAction
        fields = ['title']


class EditPromoActionDirectionsForm(forms.ModelForm):
    class Meta:
        model = PromoAction
        fields = ['directions']


class EditPromoActionCitiesForm(forms.ModelForm):
    class Meta:
        model = PromoAction
        fields = ['cities']


class EditPromoActionDescriptionForm(forms.ModelForm):
    class Meta:
        model = PromoAction
        fields = ['description']


class EditPromoActionNoteForm(forms.ModelForm):
    class Meta:
        model = PromoAction
        fields = ['note']


class EditPromoActionImageForm(forms.ModelForm):
    class Meta:
        model = PromoAction
        fields = ['image']


class EditPromoActionVideoForm(forms.ModelForm):
    class Meta:
        model = PromoAction
        fields = ['video']


class EditPromoActionDatesForm(forms.ModelForm):
    class Meta:
        model = PromoAction
        fields = ['start_date', 'end_date']


class EditPromoActionStatusForm(forms.ModelForm):
    class Meta:
        model = PromoAction
        fields = ['_status']


class EditPromoActionEventDanceClassesForm(forms.ModelForm):
    class Meta:
        model = EventLocalClasses
        fields = ['dance_styles', 'dance_directions']


class EditPromoActionLinksForm(forms.ModelForm):
    class Meta:
        model = PromoAction
        fields = ['links']


class EditPromoActionPolicyForm(forms.ModelForm):
    class Meta:
        model = PromoAction
        fields = ['owners', 'contributors', 'author']
