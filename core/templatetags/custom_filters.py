from django import template

register = template.Library()

COLORS = [
    "ctp-rosewater",
    "ctp-lavender",
    "ctp-pink",
    "ctp-sapphire",
    "ctp-red",
    "ctp-teal",
    "ctp-peach",
    "ctp-green",
]


@register.filter(name="get_color")
def get_color(value):
    return COLORS[value % len(COLORS)]
