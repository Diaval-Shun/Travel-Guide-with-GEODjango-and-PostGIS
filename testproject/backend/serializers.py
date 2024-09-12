from .models import Category, Place, Location
from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PlaceSerializer(GeoFeatureModelSerializer):
    categories = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field = 'category_name')
    class Meta:
        model = Place
        geo_field = 'point_geom'
        fields = (
            'pk',
            'categories',
            'place_name',
            'description',
            'image',
            'color',
            'created_at',
            'modified_at',
        )

class LocationSerializer(GeoFeatureModelSerializer):
    proximity = serializers.SerializerMethodField('get_proximity')

    def get_proximity(self, obj):
        if obj.distance:
            #return obj.distance.km
            return round(obj.distance.km, 2)
        return False
    
    class Meta:
        model = Location
        geo_field = 'point_geom'
        fields = (
            'pk',
            'name',
            'type',
            'proximity'
        )