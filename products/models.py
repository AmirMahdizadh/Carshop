from django.db import models

class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Slider(models.Model):
    objects = None
    img_urls = models.CharField(max_length=2083)

class Navbar(models.Model):
    title = models.CharField(max_length=100)