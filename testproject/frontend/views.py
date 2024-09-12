from django.shortcuts import render

# Create your views here.
def placesListMap(request):
    return render(request, 'frontend/places_base.html')
