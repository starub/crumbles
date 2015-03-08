from datetime import datetime
from django.db.models.sql.datastructures import DateTime
from django.test import TestCase

from advertisement.models import Advertisement
from client.models import Client


class AdvertisementTestCase(TestCase):

    def test_create_multiple_advertisements(self):
        client = Client(first_name='John', last_name='Doe')
        
        adv1 = Advertisement()
        adv2 = Advertisement()
        
        adv1.save()
        adv2.save()
