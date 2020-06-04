from django import template
register = template.Library()


@register.filter(name='cut_to_long_text')
def cut_to_long_text(value, arg):
    if len(value) >= arg :
        value = value[:arg] + '...'
    return value