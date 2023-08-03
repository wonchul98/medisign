from django.urls import path
from .views import UserList, UserDetail
from . import views
from rest_framework.authtoken import views as token_views

app_name = "users"
urlpatterns = [
    path('', views.main, name='main'),

    # /users/User_list
    path("User_list", UserList.as_view(), name = "user_list"),
    # /users/User_list/1
    path("User_list/<int:user_id>", UserDetail.as_view(), name = "user_detail"),
    # /users/auth
    path("auth", token_views.obtain_auth_token, name = "user_auth-create")
]
