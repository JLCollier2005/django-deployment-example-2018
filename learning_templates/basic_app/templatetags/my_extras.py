from django import template

register = template.Library()

#name parameter is optional. If not added, the function name will be used
@register.filter(name="cutter")
def cutter(value,arg):
    """
    Cuts out all values of 'arg' from the string
    """
    return value.replace(arg,"")

#This is how to register it if you don't use the decorator
# register.filter('cutter',cutter)
