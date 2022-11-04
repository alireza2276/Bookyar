from django import template

register = template.Library()


@register.filter
def translate_number(value):
    value = str(value)
    english_number_to_persian_table = value.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩')
    return value.translate(english_number_to_persian_table)

