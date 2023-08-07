from rest_framework import serializers
from .models import Pharmacy

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = [
            'encrypted_care_symbol', 
            'care_institution_name', 
            'city_code',
            'city_name',
            'district_code',
            'district_name',
            'subdistrict',
            'postal_code',
            'address',
            'phone_number',
            'coord_x',
            'coord_y'
        ]
