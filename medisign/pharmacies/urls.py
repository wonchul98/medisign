from django.urls import path
from . import views
from .views import PharmacyNearbyView,RegularPharmacyView  
from rest_framework.authtoken import views as token_views
from django.views.generic import TemplateView

app_name = 'pharmacies'
urlpatterns = [
    path('', views.index, name='index'),
    # pharmacies/pharmacy_list
    # path("pharmacy_list", PharmacyInfo.as_view(), name="pharmacy_list"),  # 불안정함
    # pharmacies/nearby?lat=37.50&lon=127.50&distance_km=1
    path("nearby", PharmacyNearbyView.as_view(), name='nearby'), # 반경 내 약국
    # pharmacies/show_reg?user_id=
    path('reg/<int:user_id>/', RegularPharmacyView.as_view(), name='regular_pharmacy'),
    # pharmacies/show_near?lat=37.3595704&lon=127.105399&distance_km=10
    path('show_near/', TemplateView.as_view(template_name='pharmacies/near_pharmacies.html'), name='show_near'),
    # pharmacies/show_select?pharmact_id=200
    path('show_select/', TemplateView.as_view(template_name='pharmacies/select_pharmacies.html'), name='show_select'),
    # pharmacies/detail/20
    path('detail/<int:pharmacy_id>/', views.PharmacyDetail.as_view(), name='pharmacy-detail'),
]