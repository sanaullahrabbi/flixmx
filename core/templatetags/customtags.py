from django import template
register = template.Library()

@register.filter
def splitVal(value,key):
    if value:
        value = value.split(key)
        return [x.strip(' ') for x in value[:6] if x]
    else:
        return value

@register.filter()
def humanize(value):
    if value:
        value = value.replace('_', ' ')
        return value.title()
    else:
        return value