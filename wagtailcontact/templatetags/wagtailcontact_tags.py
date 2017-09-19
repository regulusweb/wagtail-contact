from django import template

register = template.Library()


@register.filter
def bleachclean(value):
    import bleach  # noqa
    return bleach.clean(value, strip=True)
