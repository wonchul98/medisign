from rest_framework import serializers
from .models import Pharmacy

class PharmacySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    encrypted_care_symbol = serializers.CharField(required=False)
    care_institution_name = serializers.CharField(required=False)
    city_code = serializers.CharField(required=False)
    city_name = serializers.CharField(required=False)
    district_code = serializers.CharField(required=False)
    district_name = serializers.CharField(required=False)
    subdistrict = serializers.CharField(required=False)
    postal_code = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)
    coord_x = serializers.FloatField(required=False)
    coord_y = serializers.FloatField(required=False)
    
    class Meta:
        model = Pharmacy
        fields = [
            'id',
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
