# Register your models here.
from django.contrib import admin
from .models import Disease

@admin.register(Disease)
class DiseaseAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    
