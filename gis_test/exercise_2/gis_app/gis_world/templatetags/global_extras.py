from django import template
from django.template.defaultfilters import stringfilter
from django.contrib.gis.geos import Point, GEOSGeometry
#from django.template.Library import assignment_tag

register = template.Library()
#@register.filter(needs_autoescape=True)
@register.assignment_tag
def point(value):
    pnt = GEOSGeometry(value)
    print pnt
    return pnt

register.filter('point', point)

