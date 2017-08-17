from django import template
from pyparsing import basestring

register = template.Library()


@register.filter('get_instance_id')
def get_instance_id(text):
    result = ''
    words = {'/event-', '/promo-action-', '/place-', '/school-', '/teacher-'}

    for word in words:
        if word in text:
            result += text[text.find(word):text.find('/', text.find(word)+1)]

    if result.find('/') == 0:
        result = result[1:]

    return result
