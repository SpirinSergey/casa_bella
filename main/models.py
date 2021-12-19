from django.db import models


class Gallery(models.Model):
    gallery_img = models.ImageField(upload_to='images/')


class Listing(models.Model):
    CUBE = models.IntegerField()
    FLOOR = models.IntegerField()
    LINE = models.IntegerField()
    UNIT_TYPE = models.CharField(max_length=15)
    UNIT = models.IntegerField()
    VIEW = models.CharField(max_length=15)
    SQ_FT = models.IntegerField()
    PRICE = models.IntegerField()


