from django.db import models
from medisign.users import models as user_model
from medisign.medicines.models import Medicine

# Create your models here.
class Disease(models.Model):
    name = models.CharField(max_length=255) # 병명
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, null=True) # 약 종류
   