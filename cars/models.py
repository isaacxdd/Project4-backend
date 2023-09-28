from django.db import models

# Create your models here.
class Car(models.Model):
    brands = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    poster = models.CharField(max_length=200)
