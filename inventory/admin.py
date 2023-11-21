from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Asset

def duplicate_object(modeladmin, request, queryset):
    for object in queryset:
        object.id = None  # Setting 'id' to None creates a new object
        object.serial = 'NEW_SERIAL_NUMBER'  # Set new serial number or leave it to edit later
        object.assettag = 'NEW_ASSET_TAG'
        object.save()

duplicate_object.short_description = "Duplicate selected record"

# Correct placement of the decorator and definition of the admin class
@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):  # Define a proper admin class for Asset
    list_display = ['Name', 'StreetAddress', 'City']  # Adjust the fields as needed
    actions = [duplicate_object]

class LibraryAdmin(OSMGeoAdmin):
    save_as = True
    list_display = ('Name', 'StreetAddress', 'City')
    # Other configurations for LibraryAdmin
