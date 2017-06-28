# coding: utf-8

from django import forms

from entities.models import AbstractEvent
from entities.models import Event
from entities.models import PromoAction


# class AbstractEventForm(forms.ModelForm):
#     class Meta:
#         model = AbstractEvent
#         fields = ['title', 'directions', 'cities', 'local_classes', 'description', 'note', 'image', 'video',
#                   'start_date', 'end_date', '_status', 'links']
#
#     class Media:
#         js = ('//code.jquery.com/jquery-1.11.0.min.js', 'js/end_date_onchange.js')
#
#     def clean(self):
#         cleaned_data = super(AbstractEventForm, self).clean()
#
#         start_date = cleaned_data.get("start_date")
#         end_date = cleaned_data.get("end_date")
#
#         if start_date and end_date:
#             if end_date < start_date:
#                 raise forms.ValidationError("End date cannot be earlier than start date!")
#
#         return cleaned_data


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'directions', 'cities', 'local_classes', 'types', 'description', 'note', 'image', 'video',
                  'start_date', 'end_date', '_status', 'locations', 'price_types', 'experience_levels', 'repeats_type',
                  'schedule', 'links', 'owners', 'contributors', 'author']

    class Media:
        js = ('//code.jquery.com/jquery-1.11.0.min.js', 'js/end_date_onchange.js')

    def clean(self):
        cleaned_data = super(EventForm, self).clean()

        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError("End date cannot be earlier than start date!")

        return cleaned_data


class PromoActionForm(forms.ModelForm):
    class Meta:
        model = PromoAction
        fields = ['title', 'directions', 'cities', 'local_classes', 'description', 'note', 'image', 'video',
                  'start_date', 'end_date', '_status', 'links', 'owners', 'contributors', 'author']

    class Media:
        js = ('//code.jquery.com/jquery-1.11.0.min.js', 'js/end_date_onchange.js')

    def clean(self):
        cleaned_data = super(PromoActionForm, self).clean()

        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError("End date cannot be earlier than start date!")

        return cleaned_data
