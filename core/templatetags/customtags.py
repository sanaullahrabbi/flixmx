from django import template
register = template.Library()

@register.filter
def splitVal(value,key):
    if value:
        value = value.split(key)
        return [x.strip(' ') for x in value if x]
    else:
        return value