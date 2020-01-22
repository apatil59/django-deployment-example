from django import template

register = template.Library()
#use of decorater
#@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts all values of arg from string

    """
    return value.replace(arg,'')

register.filter('cut',cut)
