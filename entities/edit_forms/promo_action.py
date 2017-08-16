from django import forms

from entities.models import EventLocalClasses

from entities.models.events import PromoAction


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
