from django.test import TestCase

from client.models import Client


class ClientTestCase(TestCase):

    def test_create_client(self):
        client = Client()
        client.first_name = 'John'
        client.last_name = 'Doe'
        client.email = 'john.doe@test.com'
        client.phone = '22133441144'        
        
        client.save()
        
        self.assertTrue(Client.objects.filter(first_name = 'John') != None)