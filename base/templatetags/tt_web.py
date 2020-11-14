from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def replace(text: str, old_new):
    """
    Replace characters in a string
    :param text: Text to operate on
    :param old_new: String that describes the replacement, wih the old and new
    values separated by comma. For example, `p,g` would replace all p's with g's.
    :return:
    """
    arr = old_new.split(',')
    old = arr[0]
    new = arr[1]
    return mark_safe(text.replace(old, new))
