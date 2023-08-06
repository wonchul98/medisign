from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class PharmacyAPITestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='admin', password='1')
        
        # create token for the user
        self.token = Token.objects.create(user=self.user)
        
        # initialize APIClient and set the token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        

    def test_api_can_get_a_pharmacy(self):
        response = self.client.get(reverse('pharmacys:pharmacy_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)