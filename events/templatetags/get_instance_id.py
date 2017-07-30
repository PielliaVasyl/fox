from django import template
from pyparsing import basestring

register = template.Library()


@register.filter('get_instance_id')
def get_instance_id(text):
    result = ''
    if '/event-' in text:
        result += text[text.find('/event-'):text.find('/', text.find('/event-')+1)]
    if result.find('/') == 0:
        result = result[1:]

    return result
