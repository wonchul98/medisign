from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from medisign.pharmacies.models import Pharmacy

from django.contrib.auth import get_user_model
User = get_user_model()

class UserAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='1')
        
        # create token for the user
        self.token = Token.objects.create(user=self.user)
        
        # initialize APIClient and set the token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.pharmacy = Pharmacy.objects.create(
            encrypted_care_symbol="test_symbol",
            care_institution_name="Test Pharmacy",
            city_code="12345",
            city_name="Test City",
            district_code="6789",
            district_name="Test District",
            subdistrict="Test Subdistrict",
            postal_code="100-000",
            address="123 Test Street, Test City",
            phone_number="010-1234-5678",
            coord_x=127.0,
            coord_y=37.0
        )

    def test_api_can_create_a_user(self):
        user_data = {
            'username': 'testuser',
            'password': 'testpassword'
            # fill the rest of the data fields as necessary
        }  
        response = self.client.post(reverse('users:user_list'), user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_user(self):
        response = self.client.get(reverse('users:user_detail', kwargs={'user_id': self.user.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_update_user(self):
        myPharmacy = Pharmacy.objects.get(id=self.pharmacy.id)
        change_user = {
            "name": "New Name",
            "user_name": "new_username",
            "gender": "M",
            "weight": 70,
            "height": 180,
            "birth_date": "1995-12-17",
            "regular_pharmacy" : [myPharmacy.id],  # DB에서 가져온 Pharmacy 객체의 ID를 추가합니다.
        }

        res = self.client.put(
            reverse('users:user_detail', kwargs={'user_id': self.user.id}),
            change_user, 
            format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_user(self):
        response = self.client.delete(
            reverse('users:user_detail', kwargs={'user_id': self.user.id}), 
            format='json', 
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
