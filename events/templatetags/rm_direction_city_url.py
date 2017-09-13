from django import template

register = template.Library()


@register.filter('rm_direction_city_url')
def rm_direction_city_url(text):
    if '/direction-' in text:
        return text[:text.find('/direction-') + 1]
    if '/city-' in text:
        return text[:text.find('/city-') + 1]
    return text


