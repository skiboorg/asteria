from django import template

register = template.Library()

@register.filter
def gettext(data):
    try:
        return data.split('-')[0]
    except:
        return 'Неверно указаны разделители в описании блока'
@register.filter
def getheader(data):
    try:
        return data.split('-')[1]
    except:
        return 'Неверно указаны разделители в описании блока'