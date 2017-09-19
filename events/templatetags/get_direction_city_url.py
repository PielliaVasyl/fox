from django import template
from entities.models import Direction, City

register = template.Library()


@register.filter('get_direction_city_url')
def get_direction_city_url(session):
    result = ''
    direction_id = session.get('direction_id', 0)
    if direction_id:
        direction = Direction.objects.filter(id=direction_id).first()
        if direction:
            result += 'direction-%s/' % direction.title

    city_id = session.get('city_id', 0)
    if city_id:
        city = City.objects.filter(id=city_id).first()
        if city:
            result += 'city-%s/' % city.title

    return result


