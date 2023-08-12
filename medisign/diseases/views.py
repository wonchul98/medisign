# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import DiseaseSerializer
from .models import Disease

class DiseaseList(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        model = Disease.objects.all()
        serializer = DiseaseSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DiseaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DiseaseDetail(APIView):
    permission_classes = [AllowAny]
    def get(self, request, disease_id):
        model = Disease.objects.get(id=disease_id)
        serializer = DiseaseSerializer(model)
        return Response(serializer.data)

    def put(self, request, disease_id):
        model = Disease.objects.get(id=disease_id)
        serializer = DiseaseSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, disease_id):
        model =Disease.objects.get(id=disease_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


# Create your views here.
def index(request):
    return render(request, 'medicines/index.html')

