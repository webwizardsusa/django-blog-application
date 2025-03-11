from django import template
from django.template.loader import render_to_string

register = template.Library()

@register.simple_tag
def datatable(type, table_id=None, columns=None):
    context ={
        'type': type,
        'table_id': table_id,
        'columns': columns
    }

    return render_to_string('components/tables/ajax_dt.html', context)

@register.simple_tag
def sweetalert(type):
    context ={
        'type': type
    }

    return render_to_string('components/sweetalert.html', context)