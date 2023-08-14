from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class Medicine(models.Model):
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='media/medicine_pictures', null=True)
    entpName = models.CharField(max_length=4000, null=True)
    efcyQesitm= models.CharField(max_length=10485760, null=True)
    useMethodQesitm= models.CharField(max_length=10485760, null=True)
    atpnWarnQesitm= models.CharField(max_length=10485760, null=True)
    atpnQesitm= models.CharField(max_length=10485760, null=True)
    intrcQesitm= models.CharField(max_length=10485760, null=True)
    seQesitm= models.CharField(max_length=10485760, null=True)
    depositMethodQesitm= models.CharField(max_length=10485760, null=True)
    
    def __str__(self):
        return self.name

class Prescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='prescription_picture/' , null = True)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE) # 약 종류
    prescription_date = models.DateField(null = True) #처방 날짜
    duration = models.IntegerField(null=True)  # 복용 일수
    dosage_time = models.TimeField(null=True)  # 복용 시간
    hospital = models.CharField(null = True, max_length=255) # 약 처방 병원
    
    
    def __str__(self):
        return f"{self.user.name}'s {self.medicine.name}"
    
    