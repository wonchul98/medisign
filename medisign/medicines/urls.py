from django.urls import path, include
from . import views
from .views import MedicineList, MedicineDetail, PrescriptionViewSet
from rest_framework.authtoken import views as token_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'prescriptions', PrescriptionViewSet)

app_name = 'medicines'

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    # /medicines/medicine_list
    path("medicine_list", MedicineList.as_view(), name = "medicine_list"),
    # /medicines/medicine_list/1
    path("medicine_list/<int:medicine_id>", MedicineDetail.as_view(), name = "medicine_detail"),
    # /medicines/auth
    path("auth", token_views.obtain_auth_token, name = "medicine_auth-create")   
]