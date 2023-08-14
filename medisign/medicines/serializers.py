from rest_framework import serializers
from .models import Medicine, Prescription
from django.contrib.auth import get_user_model

User = get_user_model()

class MedicineSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(required=False)
    image = serializers.ImageField(required=False)
    
    class Meta:
        model = Medicine
        fields = '__all__'
        
        
class PrescriptionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    picture = serializers.ImageField(required = False)
    medicine = serializers.PrimaryKeyRelatedField(queryset=Medicine.objects.all(), required=False)
    prescription_date = serializers.DateField(required=False)
    duration = serializers.IntegerField(required=False)
    dosage_time = serializers.TimeField(required=False)
    hospital = serializers.CharField(required=False, max_length=255)
    
    class Meta:
        model = Prescription
        fields = ['user', 'picture', 'medicine', 'prescription_date', 'duration', 'dosage_time', 'hospital']