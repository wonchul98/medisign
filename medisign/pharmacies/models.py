from django.db import models
import math

# Create your models here.
class PharmacyManager(models.Manager):
    def from_location_within_distance(self, lat, lon, distance_km):
        # Haversine Formula
        p = math.pi / 180
        # Radius of the Earth in km
        earth_radius = 6371
        pharmacies = self.get_queryset()
        return [pharmacy for pharmacy in pharmacies
                if earth_radius * math.acos(math.sin(lat * p) * math.sin(pharmacy.coord_x * p) + math.cos(lat * p) * math.cos(pharmacy.coord_x * p) *
                                       math.cos((lon - pharmacy.coord_y) * p)) <= distance_km]

class Pharmacy(models.Model):
    encrypted_care_symbol = models.CharField(max_length=255)
    care_institution_name = models.CharField(max_length=255) #기관 명
    city_code = models.CharField(max_length=50) # 시도코드
    city_name = models.CharField(max_length=255) #시도코드명
    district_code = models.CharField(max_length=50)  # 시군구코드
    district_name = models.CharField(max_length=255) # 시군구코드명
    subdistrict = models.CharField(max_length=255) # 읍면동
    postal_code = models.CharField(max_length=50) # 우편번호
    address = models.TextField() # 주소
    phone_number = models.CharField(max_length=50)
    coord_x = models.FloatField()
    coord_y = models.FloatField()
    objects = PharmacyManager()

    def __str__(self):
        return self.care_institution_name

    