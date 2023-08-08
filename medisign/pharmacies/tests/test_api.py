from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from medisign.pharmacies.models import Pharmacy
from medisign.pharmacies.serializers import PharmacySerializer

User = get_user_model()

# class PharmacyAPITestCase(APITestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(username='admin', password='1')
        
#         # create token for the user
#         self.token = Token.objects.create(user=self.user)
        
#         # initialize APIClient and set the token
#         self.client = APIClient()
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        

#     def test_api_can_get_a_pharmacy(self):
#         response = self.client.get(reverse('pharmacies:pharmacy_list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
        



class PharmacyNearbyViewTest(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='admin', password='1')
        
        # create token for the user
        self.token = Token.objects.create(user=self.user)
        
        # initialize APIClient and set the token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        # Sample data
        self.pharmacy1 = Pharmacy.objects.create(
            encrypted_care_symbol="test1",
            care_institution_name="Test Pharmacy 1",
            city_code="110000",
            city_name="City1",
            district_code="110019",
            district_name="District1",
            subdistrict="Subdistrict1",
            postal_code="100001",
            address="Address1",
            phone_number="123456789",
            coord_x=37.50,
            coord_y=127.50,
        )

        self.pharmacy2 = Pharmacy.objects.create(
            encrypted_care_symbol="test2",
            care_institution_name="Test Pharmacy 2",
            city_code="110000",
            city_name="City2",
            district_code="110019",
            district_name="District2",
            subdistrict="Subdistrict2",
            postal_code="100002",
            address="Address2",
            phone_number="987654321",
            coord_x=38.50,
            coord_y=127.50,
        )

    def test_pharmacy_nearby_view(self):
        url = reverse('pharmacies:nearby')
        #url = 'https://medisign-hackthon-95c791df694a.herokuapp.com/pharmacies/'
        # Assuming that your endpoint is /pharmacy-nearby/?lat=37.50&lon=127.50&distance_km=1
        url = f"{url}?lat=37.50&lon=127.50&distance_km=1"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        pharmacies = Pharmacy.objects.filter(id=self.pharmacy1.id)  # Assuming Pharmacy.objects.from_location_within_distance works correctly
        serializer = PharmacySerializer(pharmacies, many=True)
        self.assertEqual(response.data, serializer.data)