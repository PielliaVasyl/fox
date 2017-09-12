from django.http import HttpResponseRedirect
from django.shortcuts import render
from entities.forms.classes import SelectCityForm, SelectDirectionForm
from entities.models import City, Direction


def _get_direction_city_url(city_id: int or None, direction_id: int or None):
    direction_city_url = ''
    direction_title, city_title = '', ''
    direction = Direction.objects.filter(id=direction_id).first()
    if direction:
        direction_title = direction.title
    city = City.objects.filter(id=city_id).first()
    if city:
        city_title = city.title
    if direction_title:
        direction_city_url += 'direction-' + direction_title + '/'
    if city_title:
        direction_city_url += 'city-' + city_title + '/'
    return direction_city_url


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

    if select_city_form.is_valid() or select_direction_form.is_valid():
        city_id = request.POST['city']
        direction_id = request.POST['direction']
        return HttpResponseRedirect('/%s' % (_get_direction_city_url(city_id, direction_id)))

    context = {
        'select_city_form': select_city_form,
        'select_direction_form': select_direction_form,
        'title': title,
        'city_title': city_title,
        'direction_title': direction_title
    }
    return render(request, 'base.html', context)
