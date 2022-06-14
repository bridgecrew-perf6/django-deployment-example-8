from django import template

register = template.Library()

@register.filter(name='cutx')
def cutx(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg, '')

@register.filter(name='bacon')
def bacon(value, arg):
    result = int(value) * int(arg)
    return result

# register.filter('cut', cut)
# register.filter('bir', bir)
