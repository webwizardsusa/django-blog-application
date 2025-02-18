from django import template
from datetime import datetime, date

register = template.Library()

@register.filter
def date_format(value, fmt="%m/%d/%Y"):
    if isinstance(value, (datetime, date)):
        return value.strftime(fmt)
    return value