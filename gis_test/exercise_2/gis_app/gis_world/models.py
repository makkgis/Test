import datetime

# from django.db import models
from django.contrib.gis.db import models
from django.utils import timezone

# Create your models here.
class Country(models.Model):
	gid = models.AutoField(primary_key=True)
	objects = models.GeoManager()
	geom = models.MultiPolygonField( srid=4326)
	question_text = models.CharField(max_length=200)
	iso2 = models.CharField('2 Digit ISO', max_length=2)
	iso3 = models.CharField('3 Digit ISO', max_length=3)
	name = models.CharField(max_length=200)
	pop2005 = models.IntegerField()
	class Meta:
		managed = False
		db_table = 'country'
	

class Hotspot(models.Model):
	gid = models.AutoField(primary_key=True)
	objects = models.GeoManager()
	geom = models.PointField(geography=True, blank=True, null=True)
	scan = models.IntegerField()
	track = models.IntegerField()
	acq_date = models.DateTimeField('Date Acquired')
	acq_time = models.CharField('Acquisition Time', max_length=5)
	satellite = models.CharField(max_length=1)
	# due to time constrains, I pulled the lat and long for accurate data points
	latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
	class Meta:
		managed = False
		db_table = 'hotspot'



