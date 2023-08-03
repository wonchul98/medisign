from django.db import models
from medisign.users import models as user_model

# Create your models here.
class Disease(models.Model):
    name = models.CharField(max_length=255) # 병명
    user = models.ForeignKey(user_model.User, on_delete=models.CASCADE, related_name='diseases')

   