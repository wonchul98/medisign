from rest_framework import serializers
from .models import User, Widget
from medisign.medicines.models import Medicine
from medisign.pharmacies.models import Pharmacy
from medisign.diseases.models import Disease
from medisign.medicines.serializers import PrescriptionSerializer
from medisign.widgets.serializers import WidgetSerializer

class Userserializer(serializers.ModelSerializer):
    
    name = serializers.CharField(required=False)
    profile_photo = serializers.ImageField(required=False)
    gender = serializers.CharField(required=False)
    weight = serializers.IntegerField(required=False)
    height = serializers.IntegerField(required=False)
    birth_date = serializers.DateField(required=False)
    blood_type = serializers.CharField(required=False)
    
    regular_pharmacy = serializers.PrimaryKeyRelatedField(many=True, queryset=Pharmacy.objects.all(), required=False)
    medicine = serializers.SerializerMethodField()
    disease = serializers.PrimaryKeyRelatedField(many=True, queryset=Disease.objects.all(), required=False)
    
    prescriptions = PrescriptionSerializer(many=True, read_only=True, required=False)
    widgets = WidgetSerializer(many=True, read_only=True, required=False)
    
    alarm =serializers.JSONField(required = False)
    dosage = serializers.JSONField(required = False)
    
    
    class Meta:
        model = User
        fields = [
            'id', 'name', 'profile_photo', 'gender', 'weight',
            'height', 'birth_date', 'blood_type', 'regular_pharmacy',
            'medicine', 'disease', 'password', 'last_login', 'is_superuser',
            'username', 'email', 'is_staff',
            'is_active', 'date_joined', 'groups',
            'prescriptions', 'widgets', 'alarm', 'dosage'
        ]
    
    def get_medicine(self, obj):
        medicines = obj.medicine.all()
        return [medicine.name for medicine in medicines]