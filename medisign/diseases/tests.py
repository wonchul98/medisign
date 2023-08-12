from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from medisign.diseases.models import Disease  # 변경: Medicine 대신 Disease 모델을 import
from medisign.diseases.serializers import DiseaseSerializer  # 변경: MedicineSerializer 대신 DiseaseSerializer를 import
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.authtoken.models import Token

from django.contrib.auth import get_user_model

User = get_user_model()

class DiseaseAPITestCase(APITestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='admin', password='1')
        
        # create token for the user
        self.token = Token.objects.create(user=self.user)
        
        # initialize APIClient and set the token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.disease = Disease.objects.create( 
            name="Test Disease"  
        )

    def test_api_can_create_a_disease(self): 
        disease_data = {'name': 'Some disease'}  
        response = self.client.post(reverse('diseases:disease_list'), disease_data, format='json')  
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_disease(self):  
        response = self.client.get(reverse('diseases:disease_detail', kwargs={'disease_id': self.disease.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
# Create your tests here.
