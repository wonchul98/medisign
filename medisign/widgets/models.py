from django.db import models
from django.contrib.postgres.fields import ArrayField

class Widget(models.Model):
    text = ArrayField(models.TextField(blank=True))
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="widgets")

    def __str__(self):
        return self.text