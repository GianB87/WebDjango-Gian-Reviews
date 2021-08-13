
from django import template

register = template.Library()

# dictonary
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

# select correct color for label
@register.filter
def qual(rate):
    return 'gray' if rate == 0 else 'orange' if rate <=3 else 'yell' if rate <= 6 else 'blue' if rate <= 8 else 'green'

@register.filter()
def to_int(value):
    return int(value)

@register.filter()
def order_title(value):
    if value == 'rate_asc':
        return 'Low Rated First'
    elif value == 'date_asc':
        return 'Oldest First'
    elif value == 'rate_desc':
        return 'High Rated First'
    else:
        return 'Newest First'

import html
@register.filter()
def html_decode(s):
    return html.unescape(s)

@register.simple_tag
def get_bootstrap_alert_msg_css_name(tags):
    return "danger" if tags == "error" else tags