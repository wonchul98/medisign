from rest_framework import serializers
from .models import User
from medisign.medicines.models import Medicine
from medisign.pharmacies.models import Pharmacy
from medisign.diseases.models import Disease

class Userserializer(serializers.ModelSerializer):
    
    name = serializers.CharField(required=False)
    user_name = serializers.CharField(required=False)
    profile_photo = serializers.ImageField(required=False)
    gender = serializers.CharField(required=False)
    weight = serializers.IntegerField(required=False)
    height = serializers.IntegerField(required=False)
    birth_date = serializers.DateField(required=False)
    blood_type = serializers.CharField(required=False)
    
    regular_pharmacy = serializers.PrimaryKeyRelatedField(many=True, queryset=Pharmacy.objects.all(), required=False)
    medicine = serializers.PrimaryKeyRelatedField(many=True, queryset=Medicine.objects.all(), required=False)
    disease = serializers.PrimaryKeyRelatedField(many=True, queryset=Disease.objects.all(), required=False)
    
    class Meta:
        model = User
        fields = '__all__'
