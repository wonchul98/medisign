from django.db import models
from medisign.users import models as user_model

# Create your models here.
class Disease(models.Model):
    name = models.CharField(max_length=255) # 병명

   