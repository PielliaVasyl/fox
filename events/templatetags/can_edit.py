from django import template

register = template.Library()


@register.filter('can_edit')
def can_edit(user, instance):
    if user.is_authenticated() and instance:
        if user in instance.owners.all() or user in instance.contributors.all():
            return True
    return False
