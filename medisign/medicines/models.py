from django.db import models
from medisign.users import models as user_model


# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(user_model.User, on_delete=models.CASCADE, related_name='medicines')
    prescription_date = models.DateField()
    image = models.ImageField(upload_to='medicines/', blank=True, null=True)