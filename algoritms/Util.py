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

    if request.user.is_authenticated():
        city_id, direction_id = request.session.get('city_id', 0), request.session.get('direction_id', 0)
    else:
        city_id, direction_id = 0, 0

    if city:
        city_id = city.id
    if direction:
        direction_id = direction.id

    select_city_form = SelectCityForm(request.POST or None, initial={'city': city_id})
    select_direction_form = SelectDirectionForm(request.POST or None, initial={'direction': direction_id})

    context['select_city_form'] = select_city_form
    context['select_direction_form'] = select_direction_form

    if select_city_form.is_valid() and select_direction_form.is_valid():
        city_id = request.POST['city']
        direction_id = request.POST['direction']
        direction_city_changed = '%s' % (get_direction_city_url(city_id, direction_id))
        if request.user.is_authenticated():
            request.user.userprofile.settings.city = City.objects.filter(id=city_id).first()
            request.user.userprofile.settings.direction = Direction.objects.filter(id=direction_id).first()
            request.user.userprofile.settings.save()
        return direction_city_changed, context

    return direction_city_changed, context


def get_session_direction_city_id(request, direction_title, city_title):
    direction_id, city_id = 0, 0
    direction = Direction.objects.filter(title=direction_title).first()
    if direction:
        direction_id = direction.id
    city = City.objects.filter(title=city_title).first()
    if city:
        city_id = city.id

    if direction_title is None and city_title is None and request.user.is_authenticated():
        if request.user.settings.direction:
            direction_id = request.user.settings.direction.id
        else:
            direction_id = 0
        if request.user.settings.city:
            city_id = request.user.settings.city.id
        else:
            city_id = 0

    return direction_id, city_id
