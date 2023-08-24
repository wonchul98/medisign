from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from medisign.pharmacies.models import Pharmacy

User = get_user_model()

class ItemSeq(models.Model):
    number = models.BigIntegerField()
    
    def __str__(self):
        return f"{self.number}"
    

# class DosageTime(models.Model):
#     time = models.TimeField()
    
#     def __str__(self):
#         return f"({self.id}) {self.time.strftime('%H:%M')}"

class Medicine(models.Model):
    name = models.CharField(max_length=255, null=True)
    image = models.URLField(max_length=500, blank=True, null=True)  # S3의 URL을 저장하기 위한 필드
    entpName = models.CharField(max_length=4000, null=True)
    itemSeq = models.ManyToManyField(ItemSeq, blank=True)
    efcyQesitm = models.TextField(null=True)
    useMethodQesitm = models.TextField(null=True)
    atpnQesitm = models.TextField(null=True)
    intrcQesitm = models.TextField(null=True)
    seQesitm = models.TextField(null=True)
    depositMethodQesitm = models.TextField(null=True)
    ingredient = models.CharField(max_length=255, null = True) # 주성분
    eng_ingredient = models.CharField(max_length=255, null = True) # 주성분영문명
    ocr_data = models.CharField(max_length=255, null = True)
    
    def __str__(self):
        return self.name

class Prescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prescriptions')
    image = models.ImageField(upload_to='prescription_picture/' , null = True, blank = True, default=None)
    medicine = models.ManyToManyField(Medicine, blank=True)  # 약 종류들
    prescription_date = models.DateField(null = True, blank = True) #처방 날짜
    duration = models.IntegerField(null=True, blank = True)  # 복용 일수
    # dosage_times = models.ManyToManyField(DosageTime, blank = True) # 복용 시간 (여러개 선택 가능)
    hospital = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name='prescriptions', null = True)
    
    def __str__(self):
        return f"{self.user.name}'s {self.medicine.name}"

class Contraindication(models.Model):
    # A에 대한 정보
    drugNameA = models.CharField(max_length=255)
    drugNumberA = models.CharField(max_length=100) # CharField를 사용했는데, 필요에 따라 다른 필드 타입으로 변경 가능
    ingredientNameA = models.CharField(max_length=255)
    companyNameA = models.CharField(max_length=255)

    # B에 대한 정보
    drugNameB = models.CharField(max_length=255)
    drugNumberB = models.CharField(max_length=100) # CharField를 사용했는데, 필요에 따라 다른 필드 타입으로 변경 가능
    ingredientNameB = models.CharField(max_length=255)
    companyNameB = models.CharField(max_length=255)

    # 상세정보
    detail = models.TextField(null = True)

    def __str__(self):
        return f"{self.drugNameA} - {self.drugNameB}"
    
# class MedicineImage(models.Model):
#     name = models.CharField(max_length=200)
#     image_hash = models.CharField(max_length=64)  # SHA-256을 사용할 경우
#     image = models.ImageField(upload_to='search_images/')
#     Prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name='medicineImages', null = True)
    