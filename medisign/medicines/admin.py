# Register your models here.
from django.contrib import admin
from .models import Medicine, Prescription, Contraindication

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    search_fields = ['name']
    
@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['user']  # other fields you want to display

    def display_medicines(self, obj):
        return ", ".join([med.name for med in obj.medicine.all()])
    
    def display_dosage_times(self, obj):
        return ", ".join([dosage_time.name for dosage_time in obj.dosage_times.all()])
    
    display_medicines.short_description = 'Medicines'
    
@admin.register(Contraindication)
class ContraindicationAdmin(admin.ModelAdmin):
    list_display = ['drugNameA', 'drugNameB', 'drugNumberA', 'drugNumberA']
    search_fields = ['drugNameA', 'drugNameB', 'drugNumberA', 'drugNumberA']

