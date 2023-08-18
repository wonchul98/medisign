from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import WidgetSerializer
from .models import Widget
from rest_framework import viewsets

# Create your views here.
class WidgetViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer
    
def index(request):
    return render(request, 'medicines/index.html')