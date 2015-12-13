import requests, zipfile, StringIO, ssl, os, datetime
from db import DB


world_24_url = 'https://firms.modaps.eosdis.nasa.gov/active_fire/shapes/zips/Global_24h.zip'

world_borders = 'http://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip'

result_24 = requests.get(world_24_url, stream=True,verify=False)
result_borders = requests.get(world_borders, stream=True,verify=False)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)


with open("%s/activity.log" % dname, "ab") as myfile:
    myfile.write("Pulling content from the server %s\n" % datetime.datetime.now())

print 'Downloading zip content'

zip1 = zipfile.ZipFile(StringIO.StringIO(result_24.content))
zip1.extractall('global')

zip2 = zipfile.ZipFile(StringIO.StringIO(result_borders.content))
zip2.extractall('global')

db = DB.getDB()
db.connect()
db.init()
db.register()
db.parseShape()


