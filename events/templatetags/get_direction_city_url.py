from django import template
# from pyparsing import basestring

register = template.Library()


@register.filter('get_direction_city_url')
def get_direction_city_url(text):
    result = ''
    if '/direction-' in text:
        result += text[text.find('/direction-'):text.find('/', text.find('/direction-')+1)+1]
    if '/city-' in text:
        result += text[text.find('/city-'):text.find('/', text.find('/city-')+1)+1]
    if '//' in result:
        result = result[:result.find('//')] + result[result.find('//')+1:]
    if result.find('/') == 0:
        result = result[1:]

    return result
