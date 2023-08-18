from django.shortcuts import render

# Create your views here.
import requests
import xml.etree.ElementTree as ET
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import PharmacySerializer
from .models import Pharmacy
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()


class PharmacyDetail(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, pharmacy_id):
        try:
            pharmacy = Pharmacy.objects.get(pk=pharmacy_id)
            serializer = PharmacySerializer(pharmacy, context={'request': request})
            return Response(serializer.data)
        except Pharmacy.DoesNotExist:
            return Response({"error": "Pharmacy not found"}, status=status.HTTP_404_NOT_FOUND)

class PharmacyNearbyView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, *args, **kwargs):
        lat = float(request.GET.get('lat'))
        lon = float(request.GET.get('lon'))
        distance_km = float(request.GET.get('distance_km'))
        pharmacies = Pharmacy.objects.from_location_within_distance(lat, lon, distance_km)
        serializer = PharmacySerializer(pharmacies, many=True)
        return Response(serializer.data)
    
class RegularPharmacyView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        
        # Accessing the related manager and getting all related pharmacies
        regular_pharmacies = user.regular_pharmacy.all()
        
        # Using the care_institution_name attribute since the Pharmacy model doesn't have a 'name' attribute
        serializer = PharmacySerializer(regular_pharmacies, many=True)
        return Response(serializer.data)
    
def index(request):
    return render(request, 'users/nothing.html')
    
    

    
