from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import LibraryProfile

@admin.register(LibraryProfile)
class LibraryProfile(OSMGeoAdmin):
    save_as = True
    list_display = ('name', "contact_email","id")