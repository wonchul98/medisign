from django.urls import path
from . import views
from .views import MedicineList, MedicineDetail
from rest_framework.authtoken import views as token_views

app_name = 'medicines'
urlpatterns = [
    path('', views.index, name='index'),
    
    # /medicines/Medicine_list
    path("Medicine_list", MedicineList.as_view(), name = "medicine_list"),
    # /medicines/Medicine_list/1
    path("Medicine_list/<int:user_id>", MedicineDetail.as_view(), name = "medicine_detail"),
    # /medicines/auth
    path("auth", token_views.obtain_auth_token, name = "medicine_auth-create")
    
]