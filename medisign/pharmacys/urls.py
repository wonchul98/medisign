from django.urls import path
from . import views
from .views import PharmacyInfo  # PharmacyInfo 추가
from rest_framework.authtoken import views as token_views

app_name = 'pharmacys'
urlpatterns = [
    path('', views.index, name='index'),
    # pharmacys/pharmacy_list
    path("pharmacy_list", PharmacyInfo.as_view(), name="pharmacy_list"),  # 추가된 라인
]