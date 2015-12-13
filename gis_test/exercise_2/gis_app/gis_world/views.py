from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render

from django.contrib.gis.geos import Point, GEOSGeometry

# from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.http import HttpResponse
#from django.template import RequestContext, loader
from django.views import generic

from .models import Country, Hotspot


class IndexView(generic.ListView):
    template_name = 'index/index.html'
    context_object_name = 'global_hotspots'
    model = Hotspot

    def get_queryset(self):
        """Return the last five hundred."""
        return Hotspot.objects.all()[:500]


class DetailView(generic.DetailView):
	# NOT USED. Detailed views are client sides
    model = Country
    template_name = 'index/detail.html'




