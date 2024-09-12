from .models import Place, Category, Location
from .serializers import CategorySerializer, PlaceSerializer, LocationSerializer
from rest_framework import generics
from django.http import Http404
from django.contrib.gis.db.models.functions import Distance
from django.shortcuts import get_object_or_404

# Create your views here.

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-list'

class CategoryDetail(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = 'category-detail'
    
class PlaceList(generics.ListAPIView):
    queryset = Place.objects.filter(active = True)
    serializer_class = PlaceSerializer
    name = 'places-list'

class PlaceDetail(generics.RetrieveAPIView):
    queryset = Place.objects.filter(active = True)
    serializer_class = PlaceSerializer
    name = 'places-detail'

class LocationList(generics.ListAPIView):
    serializer_class = LocationSerializer
    name = 'location-list'

    def get_queryset(self):
        placeID = self.request.query_params.get('placeid')
        if placeID is None:
            raise Http404
        selectedPlaceGeom = get_object_or_404(Place, pk=placeID).point_geom
        nearestCities = Location.objects.annotate(distance = Distance('point_geom', selectedPlaceGeom)).order_by('distance')[:3]
        return nearestCities