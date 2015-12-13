# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('question_text', models.CharField(max_length=200)),
                ('iso2', models.CharField(max_length=2, verbose_name=b'2 Digit ISO')),
                ('iso3', models.CharField(max_length=3, verbose_name=b'3 Digit ISO')),
                ('name', models.CharField(max_length=200)),
                ('pop2005', models.IntegerField()),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hotspot',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, geography=True, blank=True)),
                ('scan', models.IntegerField()),
                ('track', models.IntegerField()),
                ('acq_date', models.DateTimeField(verbose_name=b'Date Acquired')),
                ('acq_time', models.CharField(max_length=5, verbose_name=b'Acquisition Time')),
                ('satellite', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'hotspot',
                'managed': False,
            },
        ),
    ]
