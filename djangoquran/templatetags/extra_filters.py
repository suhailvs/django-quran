from django import template
from djangoquran.buckwalter import encode,decode

register = template.Library()


@register.filter
def zfill(value, arg):
    return str(value).zfill(arg) 


@register.filter
def buckwalter_decode(value):
    return decode(value)