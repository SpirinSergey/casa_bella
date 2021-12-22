from django.db import models


class Gallery(models.Model):
    gallery_img = models.ImageField(upload_to='images/')


class Listing(models.Model):
    FLOOR = models.IntegerField(default=0)
    UNIT_TYPE = models.CharField(null=True, max_length=20)
    BATHROOMS = models.CharField(null=True, max_length=5)
    UNIT = models.IntegerField(default=0)
    INTERIOR = models.CharField(null=True, max_length=25)
    TERRACE = models.CharField(null=True, max_length=25)
    TOTAL = models.CharField(null=True, max_length=25)
    PRICE = models.CharField(null=True, max_length=25)
    FLOOR_PLANE = models.FileField(upload_to='floor_plane/', blank=True,)


