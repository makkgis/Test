from django.contrib import admin

# Register your models here.
from models import Hotspot

from django.contrib.gis import admin

# admin.site.register(Hotspot, admin.GeoModelAdmin)

admin.site.register(Hotspot, admin.OSMGeoAdmin)