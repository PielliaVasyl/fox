from django import template

register = template.Library()


@register.filter('can_delete')
def can_delete(user, instance):
    if user.is_authenticated() and instance:
        if user in instance.owners.all():
            return True
    return False
