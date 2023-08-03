from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import MedicineSerializer
from .models import Medicine

class MedicineList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        model = Medicine.objects.all()
        serializer = MedicineSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicineDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, medicine_id):
        model = Medicine.objects.get(id=medicine_id)
        serializer = MedicineSerializer(model)
        return Response(serializer.data)

    def put(self, request, medicine_id):
        model = Medicine.objects.get(id=medicine_id)
        serializer = MedicineSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, medicine_id):
        model = Medicine.objects.get(id=medicine_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Create your views here.
def index(request):
    return render(request, 'medicines/index.html')

