from django.contrib import admin
from .models import Pharmacy

class PharmacyAdmin(admin.ModelAdmin):
    list_display = ['care_institution_name', 'city_name', 'district_name', 'phone_number', 'address']
    search_fields = ['care_institution_name', 'city_name', 'district_name', 'phone_number', 'address']
    list_filter = ['city_name', 'district_name']
    ordering = ['care_institution_name']


admin.site.register(Pharmacy, PharmacyAdmin)
    
