from django import forms

# from entities.models import DanceDirection
from entities.models import DanceStyle
from entities.models import Event
from entities.models import EventType


def _get_event_types_choices(events):
    event_type_dict = EventType.TITLE_DICT

    event_types_per_events = [[(event_type.pk, event_type_dict.get(event_type.title, event_type.title))
                               for event_type in event.types.all()]
                              for event in events]

    event_types_choices = []
    for event_types_per_event in event_types_per_events:
        event_types_choices.extend(event_types_per_event)
    event_types_choices = tuple(set(event_types_choices))

    return event_types_choices


def _get_dance_styles_choices(dance_styles, events):
    # direction_dict = DanceDirection.DIRECTION_SHOW
    all_directions = set([dance_style.dance_direction for dance_style in dance_styles])

    styles_per_event = [[(dance_style.dance_direction, dance_style.pk, dance_style.title)
                         for dance_style in event.local_classes.dance_styles.all()]
                        for event in events]
    all_dance_styles = []
    for j in styles_per_event:
        all_dance_styles.extend(j)
    all_dance_styles = tuple(set(all_dance_styles))

    dance_styles_choices = ([(dance_direction,
                              tuple([(i[1], i[2]) for i in [dance_style for dance_style in all_dance_styles]
                                     if i[0] == dance_direction])) for dance_direction in all_directions][0],)
    return dance_styles_choices


def _get_cities_choices(events):
    cities_per_events = [[(loc.city.pk, loc.city.city) for loc in event.locations.all() if loc.city]
                         for event in events]
    all_cities = []
    for cities_per_event in cities_per_events:
        all_cities.extend(cities_per_event)
    all_cities = tuple(set(all_cities))
    return all_cities


class EventsFilterForm(forms.Form):
    events = Event.objects.all()

    event_types = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите типы..."}),
        required=False,
        label='Типы мероприятий'
    )

    cities = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите города..."}),
        required=False,
        label='Города'
    )

    def __init__(self, *args, **kwargs):
        events = Event.objects.all()
        self.direction = kwargs.pop('direction')

        super(EventsFilterForm, self).__init__(*args, **kwargs)
        self.fields['event_types'].choices = _get_event_types_choices(events)
        self.fields['cities'].choices = _get_cities_choices(events)

        if self.direction == 'dance':
            dance_styles = DanceStyle.objects.all()
            self.fields['dance_styles'] = forms.MultipleChoiceField(
                widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                                   'tabindex': '0',
                                                   'data-placeholder': "Выберите танцевальные стили..."}),
                required=False,
                label='Танцевальные стили',
                choices=_get_dance_styles_choices(dance_styles, events)
                )
