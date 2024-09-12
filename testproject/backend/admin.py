from django.contrib.gis import admin
from .models import Category, Place, Location
# Register your models here.

admin.site.register(Category)

class CustomGeoAdmin(admin.GISModelAdmin):
    gis_widget_kwargs = {
        'attrs': {
            'default_zoom': 10,
            'default_lon': 106.69511151401589,
            'default_lat': 10.778920395515254
        }
    }

@admin.register(Place)
class PlaceAdmin(CustomGeoAdmin):
     pass

@admin.register(Location)
class PlaceAdmin(CustomGeoAdmin):
     pass





