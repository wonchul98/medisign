from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from django.shortcuts import render

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()



class UserList(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        model = User.objects.all()
        serializer = Userserializer(model, many = True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Userserializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    
    
class UserDetail(APIView):
    permission_classes = [AllowAny]
    def get(self, request, user_id):
        model = User.objects.get(id = user_id)
        serializer = Userserializer(model, context={'request': request})
        return Response(serializer.data)
    
    def put(self, request, user_id):
        model = User.objects.get(id = user_id)
        serializer = Userserializer(instance=model, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)  
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, user_id):
        model = User.objects.get(id = user_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


def main(request):
    return render(request, 'users/user_detail.html')

def index(request):
    return render(request, 'users/user_detail.html')