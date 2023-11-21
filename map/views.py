from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Park


longitude = -87.658073
latitude = 41.838934

user_location = Point(longitude, latitude, srid=4326)


# Create your views here.

class Home(generic.ListView):
    model = Park
    context_object_name = 'map'
    queryset = Park.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:600]
    template_name = 'index.html'