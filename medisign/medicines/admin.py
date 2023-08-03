# Register your models here.
from django.contrib import admin
from .models import Medicine, Prescription

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    search_fields = ['name']
    
@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'medicine', 'prescription_date']
    search_fields = ['user']
    