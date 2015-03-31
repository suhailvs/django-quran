from django import template

register = template.Library()
@register.filter
def zfill(value, arg):
    return str(value).zfill(arg) 