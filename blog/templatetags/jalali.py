import jdatetime
from django import template

register = template.Library()

@register.filter
def to_jalali(value):
    if not value:
        return ""

    date = jdatetime.datetime.fromgregorian(datetime=value)

    months = [
        "فروردین", "اردیبهشت", "خرداد",
        "تیر", "مرداد", "شهریور",
        "مهر", "آبان", "آذر",
        "دی", "بهمن", "اسفند"
    ]

    return f"{date.day} {months[date.month - 1]} {date.year}"