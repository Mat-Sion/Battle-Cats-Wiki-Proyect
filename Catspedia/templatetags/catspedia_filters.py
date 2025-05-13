from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return value

@register.filter
def divide(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, TypeError, ZeroDivisionError):
        return value

@register.filter
def split(value, arg):
    return value.split(arg)

@register.filter
def first(value):
    try:
        return value[0]
    except (IndexError, TypeError):
        return value