from django import template

register = template.Library()


@register.filter()
def mymedia(val):
    if val:
        return f'/media/{val}'
    return '#'


@register.simple_tag()
def mediapach(val):
    if val:
        return f'/media/{val}'
    return '#'