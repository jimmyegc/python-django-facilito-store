from django import template 

register = template.Library()

@register.filter()
def price_format(value):
    """
    Formatea el valor numérico como precio en pesos mexicanos.
    Ejemplo: 1234567.89 -> $1,234,567.89
    """
    try:
        value = float(value)
        return "${:,.2f}".format(value)
    except (ValueError, TypeError):
        return "$0.00"