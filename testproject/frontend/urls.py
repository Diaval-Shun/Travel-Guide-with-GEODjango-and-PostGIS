from django.urls import path
from . import views

app_name = 'frontend'#officially 

urlpatterns = [
    path('', views.placesListMap, name = 'places_list_map'),
]