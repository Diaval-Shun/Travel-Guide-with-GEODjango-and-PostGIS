from django.db import models
from django.contrib.gis.db import models
# Create your models here.

class Category(models.Model):
    category_name = models.CharField('Category name', max_length=50, help_text='Specify a cultural heritage category')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name
    
class Place(models.Model):
    categories = models.ForeignKey('Category', on_delete=models.CASCADE)
    place_name = models.CharField('Place name', max_length=50)
    color = models.CharField('Place Color', max_length=50, default="green")
    description = models.TextField('Place description', blank=True)
    image = models.ImageField(upload_to="place_images/", blank=True, null=True)
    active = models.BooleanField(default=True)
    point_geom = models.PointField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Places'

    def __str__(self):
        return self.place_name
    
class Location(models.Model):
    #places = models.ForeignKey('Place', default=3, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    type = models.CharField(default='station')
    point_geom = models.PointField()

    class Meta:
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.name
 

    