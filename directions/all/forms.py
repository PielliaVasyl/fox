from django import forms

# from entities.models import DanceDirection
from entities.models import DanceStyle
from entities.models import Event
from entities.models import EventType
from entities.models.pages import Place, School, Shop, CustomerServices, Hall
from entities.models.types import PlaceType, ShopType, CustomerServicesType


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


def _get_dance_styles_choices(dance_styles, instances):
    # direction_dict = DanceDirection.DIRECTION_SHOW
    all_dance_directions = set([dance_style.dance_direction for dance_style in dance_styles])

    styles_per_event = [[(dance_style.dance_direction, dance_style.pk, dance_style.title)
                         for dance_style in event.local_classes.dance_styles.all()]
                        for event in instances]
    all_dance_styles = []
    for j in styles_per_event:
        all_dance_styles.extend(j)
    all_dance_styles = tuple(set(all_dance_styles))

    dance_styles_choices = ([(dance_direction,
                              tuple([(i[1], i[2]) for i in [dance_style for dance_style in all_dance_styles]
                                     if i[0] == dance_direction])) for dance_direction in all_dance_directions][0],)
    return dance_styles_choices


def _get_instances_choices(instances):
    instances = [(instance.pk, instance.title) for instance in instances]

    instances = tuple(set(instances))
    return instances


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

    cities = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите города..."}),
        required=False,
        label='Города'
    )

    event_types = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите типы..."}),
        required=False,
        label='Типы мероприятий'
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


def _get_place_types_choices(places):
    place_type_dict = PlaceType.TITLE_DICT

    place_types_per_places = [[(place_type.pk, place_type_dict.get(place_type.title, place_type.title))
                               for place_type in place.types.all()]
                              for place in places]

    place_types_choices = []
    for place_types_per_place in place_types_per_places:
        place_types_choices.extend(place_types_per_place)
    place_types_choices = tuple(set(place_types_choices))

    return place_types_choices


def _get_shop_types_choices(shops):
    shop_type_dict = ShopType.TITLE_DICT

    shop_types_per_shops = [[(shop_type.pk, shop_type_dict.get(shop_type.title, shop_type.title))
                             for shop_type in shop.types.all()]
                            for shop in shops]

    shop_types_choices = []
    for shop_types_per_shop in shop_types_per_shops:
        shop_types_choices.extend(shop_types_per_shop)
    shop_types_choices = tuple(set(shop_types_choices))

    return shop_types_choices


def _get_customer_services_types_choices(instances):
    instance_type_dict = CustomerServicesType.TITLE_DICT

    instance_types_per_instances = [[(instance_type.pk, instance_type_dict.get(instance_type.title,
                                                                               instance_type.title))
                                     for instance_type in instance.types.all()]
                                    for instance in instances]

    instance_types_choices = []
    for instance_types_per_instance in instance_types_per_instances:
        instance_types_choices.extend(instance_types_per_instance)
    instance_types_choices = tuple(set(instance_types_choices))

    return instance_types_choices


class PlacesFilterForm(forms.Form):
    city = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                   'tabindex': '0',
                                   'data-placeholder': "Выберите город..."}),
        required=False,
        label='Город'
    )

    places = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите место..."}),
        required=False,
        label='Места'
    )

    place_types = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите типы..."}),
        required=False,
        label='Типы мест'
    )

    def __init__(self, *args, **kwargs):
        self.direction = kwargs.pop('direction')
        if self.direction:
            current_places = Place.objects.filter(directions__title=self.direction)
        else:
            current_places = Place.objects.all()
        print(self.direction)
        super(PlacesFilterForm, self).__init__(*args, **kwargs)
        self.fields['city'].choices = _get_cities_choices(current_places)
        self.fields['places'].choices = _get_instances_choices(current_places)
        self.fields['place_types'].choices = _get_place_types_choices(current_places)

        if self.direction == 'dance':
            dance_styles = DanceStyle.objects.all()
            self.fields['dance_styles'] = forms.MultipleChoiceField(
                widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                                   'tabindex': '0',
                                                   'data-placeholder': "Выберите танцевальные стили..."}),
                required=False,
                label='Стили танцев',
                choices=_get_dance_styles_choices(dance_styles, current_places)
                )


class SchoolsFilterForm(forms.Form):
    city = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                   'tabindex': '0',
                                   'data-placeholder': "Выберите город..."}),
        required=False,
        label='Город'
    )

    schools = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите школы..."}),
        required=False,
        label='Школы'
    )

    def __init__(self, *args, **kwargs):
        self.direction = kwargs.pop('direction')
        if self.direction:
            current_schools = School.objects.filter(directions__title=self.direction)
        else:
            current_schools = School.objects.all()

        super(SchoolsFilterForm, self).__init__(*args, **kwargs)
        self.fields['city'].choices = _get_cities_choices(current_schools)
        self.fields['schools'].choices = _get_instances_choices(current_schools)

        if self.direction == 'dance':
            dance_styles = DanceStyle.objects.all()
            self.fields['dance_styles'] = forms.MultipleChoiceField(
                widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                                   'tabindex': '0',
                                                   'data-placeholder': "Выберите танцевальные стили..."}),
                required=False,
                label='Стили танцев',
                choices=_get_dance_styles_choices(dance_styles, current_schools)
                )


class ShopsFilterForm(forms.Form):
    city = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                   'tabindex': '0',
                                   'data-placeholder': "Выберите город..."}),
        required=False,
        label='Город'
    )

    shops = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите магазины..."}),
        required=False,
        label='Магазины'
    )

    shop_types = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите типы..."}),
        required=False,
        label='Типы магазинов'
    )

    def __init__(self, *args, **kwargs):
        self.direction = kwargs.pop('direction')
        if self.direction:
            current_shops = Shop.objects.filter(directions__title=self.direction)
        else:
            current_shops = Shop.objects.all()

        super(ShopsFilterForm, self).__init__(*args, **kwargs)
        self.fields['city'].choices = _get_cities_choices(current_shops)
        self.fields['shops'].choices = _get_instances_choices(current_shops)
        self.fields['shop_types'].choices = _get_shop_types_choices(current_shops)


class CustomerServicesFilterForm(forms.Form):
    city = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                   'tabindex': '0',
                                   'data-placeholder': "Выберите город..."}),
        required=False,
        label='Город'
    )

    customer_services_set = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите услуги..."}),
        required=False,
        label='Услуги'
    )

    customer_services_types = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите типы..."}),
        required=False,
        label='Типы услуг'
    )

    def __init__(self, *args, **kwargs):
        self.direction = kwargs.pop('direction')
        if self.direction:
            current_customer_services_set = CustomerServices.objects.filter(directions__title=self.direction)
        else:
            current_customer_services_set = CustomerServices.objects.all()

        super(CustomerServicesFilterForm, self).__init__(*args, **kwargs)
        self.fields['city'].choices = _get_cities_choices(current_customer_services_set)
        self.fields['customer_services_set'].choices = _get_instances_choices(current_customer_services_set)
        self.fields['customer_services_types'].choices = \
            _get_customer_services_types_choices(current_customer_services_set)


class HallsFilterForm(forms.Form):
    city = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                   'tabindex': '0',
                                   'data-placeholder': "Выберите город..."}),
        required=False,
        label='Город'
    )

    halls = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите залы..."}),
        required=False,
        label='Залы'
    )

    def __init__(self, *args, **kwargs):
        self.direction = kwargs.pop('direction')
        if self.direction:
            current_halls = Hall.objects.filter(directions__title=self.direction)
        else:
            current_halls = Hall.objects.all()

        super(HallsFilterForm, self).__init__(*args, **kwargs)
        self.fields['city'].choices = _get_cities_choices(current_halls)
        self.fields['halls'].choices = _get_instances_choices(current_halls)
