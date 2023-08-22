from rest_framework import serializers
from .models import Medicine, Prescription,DosageTime, ItemSeq, Contraindication
from django.contrib.auth import get_user_model


User = get_user_model()

class ItemSeqSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemSeq
        fields = ('number',)

class DosageTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DosageTime
        fields = ('id', 'time',)


class MedicineSerializer(serializers.ModelSerializer):
    itemSeq = serializers.SerializerMethodField()
    class Meta:
        model = Medicine
        fields = (
            'name',
            'image',
            'entpName',
            'itemSeq',
            'efcyQesitm',
            'useMethodQesitm',
            'atpnQesitm',
            'intrcQesitm',
            'seQesitm',
            'depositMethodQesitm',
            'ingredient',
            'eng_ingredient',
        )
        
    def get_itemSeq(self, obj):
        return [item.number for item in obj.itemSeq.all()]
   
        
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


class ContraindicationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contraindication
        fields = ['drugNameA', 'drugNumberA', 'ingredientNameA', 'companyNameA', 'drugNameB', 'drugNumberB', 'ingredientNameB', 'companyNameB', 'detail']
