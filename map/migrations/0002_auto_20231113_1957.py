
from django.db import migrations
import json
from django.contrib.gis.geos import fromstr
from pathlib import Path

DATA_FILENAME = 'park2.json'
def load_data(apps, schema_editor):
 Park = apps.get_model('map', 'Park')
 jsonfile = Path(__file__).parents[2] / DATA_FILENAME


 with open(str(jsonfile)) as datafile:
     objects = json.load(datafile)
     for obj in objects["elements"]:
         try:
                 name = obj.get('Name')
                 longitude = obj.get('lon', 0)
                 latitude = obj.get('lat', 0)
                 location = fromstr(f'POINT({longitude} {latitude})', srid=4326)
                 Park(name=name, location = location).save()
         except KeyError:
             pass

class Migration(migrations.Migration):


 dependencies = [
     ("map", "0001_initial"),
 ]

 operations = [
     migrations.RunPython(load_data)
 ]
