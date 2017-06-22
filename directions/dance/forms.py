from django import forms

# from entities.models import DanceDirection
from entities.models import DanceStyle
from entities.models.types import DanceStyleCountType, DanceStyleDistanceType


def _get_titles_choices(dance_style_in_section_list):
    titles_choices = [(dance_style_in_section.pk, dance_style_in_section.title)
                      for dance_style_in_section in dance_style_in_section_list]

    return titles_choices


def _get_directions_choices(dance_styles):
    # direction_show = DanceDirection.TITLE_SHOW
    directions_choices = [(dance_style.group.pk, dance_style.group.title) for dance_style in dance_styles]
    if directions_choices:
        directions_choices = tuple(set(directions_choices))

    return directions_choices


def _get_count_types_choices(dance_styles):
    count_type_dict = DanceStyleCountType.TITLE_SHOW

    count_types_per_dance_styles = [[(count_type.pk,
                                      count_type_dict.get(count_type.title, count_type.title))
                                     for count_type in dance_style.count_types.all()]
                                    for dance_style in dance_styles]

    count_types_choices = []
    for count_types_per_dance_style in count_types_per_dance_styles:
        count_types_choices.extend(count_types_per_dance_style)
    count_types_choices = tuple(set(count_types_choices))

    return count_types_choices


def _get_distances_choices(dance_styles):
    distance_dict = DanceStyleDistanceType.TITLE_SHOW

    distances_per_dance_styles = [[(distance.pk, distance_dict.get(distance.title, distance.title))
                                   for distance in dance_style_in_section.distance_types.all()]
                                  for dance_style_in_section in dance_styles]

    distances_choices = []
    for distances_per_dance_style in distances_per_dance_styles:
        distances_choices.extend(distances_per_dance_style)
    distances_choices = tuple(set(distances_choices))

    return distances_choices


# def _get_prices_choices(dance_style_in_section_list):
#     price_dict = DanceStyleInSectionAveragePrice.PRICE_SHOW
#
#     prices_per_dance_style_in_section_list = \
#         [[(price.pk, price_dict.get(price.price, price.price))
#           for price in dance_style_in_section.average_prices.all()]
#          for dance_style_in_section in dance_style_in_section_list]
#
#     prices_choices = []
#     for prices_per_dance_style_in_section in prices_per_dance_style_in_section_list:
#         prices_choices.extend(prices_per_dance_style_in_section)
#     prices_choices = tuple(set(prices_choices))
#
#     return prices_choices


class DanceStyleFilterForm(forms.Form):
    titles = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите по названию..."}),
        required=False,
        label='Название стиля'
    )

    groups = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите направления..."}),
        required=False,
        label='Направление стиля'
    )

    count_types = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите количество..."}),
        required=False,
        label='Количество людей'
    )

    distance_types = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите растояние..."}),
        required=False,
        label='Растояние между партнерами'

    )

    # average_prices = forms.MultipleChoiceField(
    #     widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
    #                                        'tabindex': '0',
    #                                        'data-placeholder': "Выберите цены..."}),
    #     choices=_get_prices_choices(dance_style_in_section_list)
    # )

    # cities = forms.MultipleChoiceField(
    #     widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
    #                                        'tabindex': '0',
    #                                        'data-placeholder': "Выберите города..."}),
    #     # choices=_get_cities_choices(events)
    # )

    def __init__(self, *args, **kwargs):
        dance_styles = DanceStyle.objects.all()

        # first call parent's constructor
        super(DanceStyleFilterForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['titles'].required = False
        self.fields['titles'].label = 'Название стиля'
        self.fields['titles'].choices = _get_titles_choices(dance_styles)
        self.fields['groups'].required = False
        self.fields['groups'].label = 'Направление стиля'
        self.fields['groups'].choices = _get_directions_choices(dance_styles)
        self.fields['count_types'].required = False
        self.fields['count_types'].label = 'Количество людей'
        self.fields['count_types'].choices = _get_count_types_choices(dance_styles)
        self.fields['distance_types'].required = False
        self.fields['distance_types'].label = 'Дистанция между партнерами'
        self.fields['distance_types'].choices = _get_distances_choices(dance_styles)
        # self.fields['average_prices'].required = False
        # self.fields['average_prices'].label = 'Уровень цен'
        # self.fields['average_prices'].choices = _get_prices_choices(dance_styles)
