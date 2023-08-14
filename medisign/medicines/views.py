from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import MedicineSerializer, PrescriptionSerializer
from .models import Medicine, Prescription
from rest_framework import viewsets

class MedicineList(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        model = Medicine.objects.all()
        serializer = MedicineSerializer(model, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = MedicineSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicineDetail(APIView):
    permission_classes = [AllowAny]
    def get(self, request, medicine_id):
        model = Medicine.objects.get(id=medicine_id)
        serializer = MedicineSerializer(model, context={'request': request})
        return Response(serializer.data)

    def put(self, request, medicine_id):
        model = Medicine.objects.get(id=medicine_id)
        serializer = MedicineSerializer(model, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, medicine_id):
        model = Medicine.objects.get(id=medicine_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    

class PrescriptionViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

# Create your views here.
def index(request):
    return render(request, 'medicines/index.html')

