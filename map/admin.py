from django.contrib import admin

# Register your models here.
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Park

@admin.register(Park)
class ParkAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')