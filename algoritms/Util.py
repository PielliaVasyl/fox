from entities.forms.classes import SelectCityForm, SelectDirectionForm
from entities.models import City
from entities.models import Direction


def get_direction_city_url(city_id: int or None, direction_id: int or None):
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


def get_is_direction_city_changed(request, city_title, direction_title):
    direction_city_changed = None
    context = {}

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

    context['select_city_form'] = select_city_form
    context['select_direction_form'] = select_direction_form

    if select_city_form.is_valid() and select_direction_form.is_valid():
        city_id = request.POST['city']
        direction_id = request.POST['direction']
        direction_city_changed = '%s' % (get_direction_city_url(city_id, direction_id))
        return direction_city_changed, context

    return direction_city_changed, context


def get_session_direction_city_id(direction_title, city_title):
    direction_id, city_id = 0, 0
    direction = Direction.objects.filter(title=direction_title).first()
    if direction:
        direction_id = direction.id
    city = City.objects.filter(title=city_title).first()
    if city:
        city_id = city.id
    return direction_id, city_id
