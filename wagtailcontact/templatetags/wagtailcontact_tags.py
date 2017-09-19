from django import template

import bleach

register = template.Library()


@register.filter
def bleachclean(value):
    return bleach.clean(value, strip=True)
