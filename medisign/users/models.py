from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from medisign.pharmacies.models import Pharmacy
from medisign.widgets.models import Widget
import json

class User(AbstractUser):
    """
    Default custom user model for medisign.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('C', 'Custom'),
    ]
    BLOOD_CHOICES = [
        ('A+', 'A Positive'),
        ('A-', 'A Negative'),
        ('B+', 'B Positive'),
        ('B-', 'B Negative'),
        ('AB+', 'AB Positive'),
        ('AB-', 'AB Negative'),
        ('O+', 'O Positive'),
        ('O-', 'O Negative'),
    ]

    # First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_name = models.CharField(blank=True, max_length=255)
    profile_photo = models.ImageField(blank=True)
    gender = models.CharField(blank=True, choices=GENDER_CHOICES, max_length=255)
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    birth_date = models.DateField(blank = True, null=True)
    blood_type = models.CharField(blank = True, choices=BLOOD_CHOICES, max_length=255)
    
    regular_pharmacy = models.ManyToManyField(Pharmacy, blank = True, related_name='users')
    medicine = models.ManyToManyField('medicines.Medicine', blank = True, related_name='users')
    disease = models.ManyToManyField('diseases.Disease', blank = True, related_name='users')


    def get_absolute_url(self) -> str:
        
        return reverse("users:detail", kwargs={"username": self.username})