# coding: utf-8

from django import forms
from django.db.models.fields.reverse_related import ManyToOneRel, ManyToManyRel
from django.contrib import admin

from entities.models import Event
from entities.models import PromoAction
from entities.models.classes import Direction


class EventForm(forms.ModelForm):
    # directions = forms.ModelMultipleChoiceField(queryset=Direction.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # RelatedFieldWidgetWrapper wants a widget to wrap, a relationship, and an admin site.
        # The widget is easy. I build the relationship manually and use the admin_site I added when the
        #  ModelAdmin was created.

        # rel = ManyToOneRel(None, Direction, 'id')
        # rel = ManyToManyRel(Event, Direction)
        # self.fields['directions'].widget = admin.widgets.RelatedFieldWidgetWrapper(self.fields['directions'].widget,
        #                                                                            Event._meta.get_field('directions').rel,
        #                                                                            self.admin_site,
        #                                                                            can_add_related=True)
        # self.fields['directions'].queryset = Direction.objects.filter(event=self.instance.pk)
        # self.fields['directions'].empty_label = None

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


class CutEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'author']


class CutPromoActionForm(forms.ModelForm):
    class Meta:
        model = PromoAction
        fields = ['title', 'author']


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
