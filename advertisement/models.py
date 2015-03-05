from django.db import models

from client.models import Client

class AdvertisementPhoto(models.Model):
    name = models.CharField(max_length=100)
    content = models.BinaryField(b"")

class AdvertisementCategory(models.Model):
    name = models.CharField(max_length=100)
    
class Advertisement(models.Model):
    client = models.ForeignKey(Client)
    category = models.ForeignKey(AdvertisementCategory)
    photo = models.ForeignKey(AdvertisementPhoto)
    description = models.CharField(max_length=1000)
    created_on = models.DateField()
    expires_on = models.DateField()


