from rest_framework import serializers
from .models import Medicine, Prescription,DosageTime
from django.contrib.auth import get_user_model

User = get_user_model()

class DosageTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DosageTime
        fields = ('id', 'time',)


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'
        
   
        
class PrescriptionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    image = serializers.SerializerMethodField(required=False)
    medicine = serializers.StringRelatedField(many=True)  
    prescription_date = serializers.DateField(required=False)
    duration = serializers.IntegerField(required=False)
    dosage_times = serializers.PrimaryKeyRelatedField(many=True, queryset=DosageTime.objects.all(), required=False)
    hospital = serializers.CharField(required=False, max_length=255)
    
    class Meta:
        model = Prescription
        fields = '__all__'
    
    def get_image(self, obj):
        if obj.image and hasattr(obj.image, 'url'):  
            return self.context['request'].build_absolute_uri(obj.image.url)
        return None