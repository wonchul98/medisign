from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Medicine(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='medicines/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Prescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    prescription_date = models.DateField()
    
    def __str__(self):
        return f"{self.user.name}'s {self.medicine.name}"
    
    