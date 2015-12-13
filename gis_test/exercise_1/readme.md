## gis
Exercise 1 (3 points)

The Earth Observing System Data and Information System by NASA disseminates MODIS

active fires data for the last 24, 48 hours and 7 days in a series of formats:

https://earthdata.nasa.gov/earth­observation­data/near­real­time/firms/active­fire­data

Develop a script that, scheduled daily with crontab, will append the 24h World shapefile

(https://firms.modaps.eosdis.nasa.gov/active_fire/shapes/zips/Global_24h.zip) to a PostGIS

table named “hotspot”.

The same PostGIS database should contain another geometric table, named “country”,

derived from this shapefile:

http://thematicmapping.org/downloads/TM_WORLD_BORDERS­0.3.zip

Using the “country” table, the script should also generate, as an additional step, a distinct

shapefile with the hotspots for each country within an output directory named “shapefiles”.

Each shapefile name should be the country ISO code contained in the “iso3” field of the

“country” table. For example, the BRA.shp shapefile will contain the daily hotspots for Brazil.

The script should be developed using shell scripting or Python and GDAL/OGR.


Step 1. Requires pip for dependency injection. For more information, please go here https://pip.pypa.io/en/latest/installing.html

```pip install -r requirements.txt```

once the requirements are installed run 

```python main.py```

The scripts will automate the install process.

Exercise 2 (7 points)

Develop a web GIS application prototype using the following technologies:

● the Django web framework
● the PostgreSQL RDBMS
● the PostGIS spatial database
● OpenLayers or Leaflet as the mapping client

The application should be composed of the following models and views:

Install dependencies
Setup the same DB used for step 1 under settings.py
browse to ``` localhost:8000 ```

##Application Screen Shots

![Main Screen](/assets/main.jpg) 

![Main Screen](/assets/info.jpg) 

![Main Screen](/assets/detail.jpg) 



