from django import template
from datetime import datetime, date
import re

register = template.Library()

@register.filter
def date_format(value, fmt="%b %d, %Y"):
    if isinstance(value, (datetime, date)):
        return value.strftime(fmt)
    return value

@register.filter
def truncate_html(value, arg):
    """
    Strips HTML tags and truncates the content to a specified length.
    """
    length = int(arg)

    if not value:
        return value

    stripped = re.sub(r'<[^>]*>', '', value)

    if len(stripped) > length:
        truncated = stripped[:length]
        truncated = truncated.rsplit(' ', 1)[0] + '...'  
        return truncated

    return stripped 