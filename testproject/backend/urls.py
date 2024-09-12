from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name = views.CategoryList.name),
    path('categories/<int:pk>', views.CategoryDetail.as_view(), name = views.CategoryDetail.name),

    path('places/', views.PlaceList.as_view(), name = views.PlaceList.name),
    path('places/<int:pk>', views.PlaceDetail.as_view(), name = views.PlaceDetail.name),

    path('locations/', views.LocationList.as_view(), name = views.LocationList.name),
]