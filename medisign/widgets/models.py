from django.db import models

class Widget(models.Model):
    text = models.TextField(blank=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name="widgets")

    def __str__(self):
        return self.text