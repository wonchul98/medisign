from rest_framework import serializers
from .models import Disease

class DiseaseSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=False)

    class Meta:
        model = Disease
        fields = '__all__'