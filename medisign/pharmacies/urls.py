from django.urls import path
from . import views
from .views import PharmacyNearbyView  
from rest_framework.authtoken import views as token_views

app_name = 'pharmacies'
urlpatterns = [
    path('', views.index, name='index'),
    # pharmacies/pharmacy_list
    # path("pharmacy_list", PharmacyInfo.as_view(), name="pharmacy_list"),  # 불안정함
    # pharmacies/nearby?lat=37.50&lon=127.50&distance_km=1
    path("nearby", PharmacyNearbyView.as_view(), name='nearby'), # 반경 내 약국
    
]