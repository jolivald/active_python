from django import template

register = template.Library()


#def lookup(object, property):
#  return getattr(object, property)
#register.simple_tag(lookup)

@register.filter
def attr(object, property):
  return getattr(object, property)
