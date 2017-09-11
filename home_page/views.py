from django.shortcuts import render
from entities.forms.classes import SelectCityForm, SelectDirectionForm
from entities.models import City, Direction


def index(request, city_title=None, direction_title=None):
    title = 'Сообщество активных людей'
    city = City.objects.filter(title=city_title).first()
    direction = Direction.objects.filter(title=direction_title).first()
    if city:
        select_city_form = SelectCityForm(request.POST or None, initial={'city': city.pk})
    else:
        select_city_form = SelectCityForm(request.POST or None)

    if direction:
        select_direction_form = SelectDirectionForm(request.POST or None, initial={'direction': direction.pk})
    else:
        select_direction_form = SelectDirectionForm(request.POST or None)

    # if select_city_form.is_valid() or select_direction_form.is_valid():
    #

    context = {
        'select_city_form': select_city_form,
        'select_direction_form': select_direction_form,
        'title': title,
        'city_title': city_title,
        'direction_title': direction_title
    }
    return render(request, 'base.html', context)
