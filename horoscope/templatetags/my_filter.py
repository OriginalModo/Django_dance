from django import template

register = template.Library()

# Создания фильтра аналог split()
@register.filter(name='split')
def split(value, key=' '):
    return value.split(key)
