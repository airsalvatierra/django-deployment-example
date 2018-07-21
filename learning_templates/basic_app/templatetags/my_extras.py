from django import template

register = template.Library()

@register.filter(name='cut') #Registrar la funcion mediante decorators
def cut(value,arg):
    """
    This cuts all values of "arg" from the string!
    """
    return value.replace(arg,'')

# Manera de registrar la funcion
# register.filter('cut',cut)
