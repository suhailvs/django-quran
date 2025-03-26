from django import template
from djangoquran2.buckwalter import encode,decode

register = template.Library()


@register.filter
def zfill(value, arg):
    return str(value).zfill(arg) 


@register.filter
def buckwalter_decode(value):
    return decode(value)

@register.filter
def times(value):
    return range(value)