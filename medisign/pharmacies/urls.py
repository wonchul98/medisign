from django.urls import path
from . import views
from .views import PharmacyNearbyView  
from rest_framework.authtoken import views as token_views
from django.views.generic import TemplateView

app_name = 'pharmacies'
urlpatterns = [
    path('', views.index, name='index'),
    # pharmacies/pharmacy_list
    # path("pharmacy_list", PharmacyInfo.as_view(), name="pharmacy_list"),  # 불안정함
    # pharmacies/nearby?lat=37.50&lon=127.50&distance_km=1
    path("nearby", PharmacyNearbyView.as_view(), name='nearby'), # 반경 내 약국
    # http://127.0.0.1:8000/pharmacies/show_near?lat=37.3595704&lon=127.105399&distance_km=10
    path('show_near/', TemplateView.as_view(template_name='pharmacies/near_pharmacies.html'), name='show_near'),
    
]