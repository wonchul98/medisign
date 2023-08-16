from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class DosageTime(models.Model):
    time = models.TimeField()
    
    def __str__(self):
        return f"({self.id}) {self.time.strftime('%H:%M')}"

class Medicine(models.Model):
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='medicine_pictures/', null=True, blank = True, default=None)
    entpName = models.CharField(max_length=4000, null=True)
    itemSeq = models.IntegerField(null = True)
    efcyQesitm= models.CharField(max_length=10485760, null=True)
    useMethodQesitm= models.CharField(max_length=10485760, null=True) #사용법
    atpnWarnQesitm= models.CharField(max_length=10485760, null=True) #주의사항경고
    atpnQesitm= models.CharField(max_length=10485760, null=True)#주의사항
    intrcQesitm= models.CharField(max_length=10485760, null=True)#상호작용
    seQesitm= models.CharField(max_length=10485760, null=True)#부작용
    depositMethodQesitm= models.CharField(max_length=10485760, null=True)#보관법
    
    def __str__(self):
        return self.name

class Prescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prescriptions')
    image = models.ImageField(upload_to='prescription_picture/' , null = True, blank = True, default=None)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, blank = True, null = True) # 약 종류
    prescription_date = models.DateField(null = True, blank = True) #처방 날짜
    duration = models.IntegerField(null=True, blank = True)  # 복용 일수
    dosage_times = models.ManyToManyField(DosageTime, blank = True) # 복용 시간 (여러개 선택 가능)
    hospital = models.CharField(null = True, max_length=255) # 약 처방 병원
    
    
    def __str__(self):
        return f"{self.user.name}'s {self.medicine.name}"
    
    