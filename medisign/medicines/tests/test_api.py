from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from medisign.medicines.models import Medicine
from medisign.medicines.serializers import MedicineSerializer
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model

User = get_user_model()

class MedicineAPITestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='admin', password='1')
        
        # create token for the user
        self.token = Token.objects.create(user=self.user)
        
        # initialize APIClient and set the token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.medicine = Medicine.objects.create(
            name="Test Medicine",

            # fill in the rest of the fields here
        )

    def test_api_can_create_a_medicine(self):
        medicine_data = {'name': 'Some medicine'}  # update this with all necessary fields
        response = self.client.post(reverse('medicines:medicine_list'), medicine_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_medicine(self):
        response = self.client.get(reverse('medicines:medicine_detail', kwargs={'medicine_id': self.medicine.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_update_medicine(self):
        change_medicine = {'name': 'Something new'}
        res = self.client.put(
            reverse('medicines:medicine_detail', kwargs={'medicine_id': self.medicine.id}),
            change_medicine, 
            format='multipart'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_medicine(self):
        medicine = Medicine.objects.get()
        response = self.client.delete(
            reverse('medicines:medicine_detail', kwargs={'medicine_id': medicine.id}), 
            format='json', 
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)