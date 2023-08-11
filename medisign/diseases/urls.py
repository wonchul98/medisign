from django.urls import path
from . import views
from .views import DiseaseList, DiseaseDetail
from rest_framework.authtoken import views as token_views

app_name = 'diseases'
urlpatterns = [
    path('', views.index, name='index'),
    
    # /disease/disease_list
    path("disease_list", DiseaseList.as_view(), name = "disease_list"),
    # /disease/disease_list/1
    path("disease_list/<int:medicine_id>", DiseaseDetail.as_view(), name = "disease_detail"),
    # /medicines/auth
    path("auth", token_views.obtain_auth_token, name = "disease_auth-create")   
]