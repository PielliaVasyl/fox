from django import forms

from entities.models.events import Event


# class EditTitleForm(forms.ModelForm):
#     title = forms.CharField(label='Название', max_length=100)


class EditTitleForm(forms.ModelForm):
    # directions = forms.ModelMultipleChoiceField(queryset=Direction.objects.all(), required=False)

    class Meta:
        model = Event
        fields = ['title']


class EditDirectionsForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['directions']
