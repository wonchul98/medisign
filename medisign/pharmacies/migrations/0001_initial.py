# Generated by Django 4.2.4 on 2023-08-07 04:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pharmacy",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("encrypted_care_symbol", models.CharField(max_length=255)),
                ("care_institution_name", models.CharField(max_length=255)),
                ("city_code", models.CharField(max_length=50)),
                ("city_name", models.CharField(max_length=255)),
                ("district_code", models.CharField(max_length=50)),
                ("district_name", models.CharField(max_length=255)),
                ("subdistrict", models.CharField(max_length=255)),
                ("postal_code", models.CharField(max_length=50)),
                ("address", models.TextField()),
                ("phone_number", models.CharField(max_length=50)),
                ("coord_x", models.FloatField()),
                ("coord_y", models.FloatField()),
            ],
        ),
    ]
