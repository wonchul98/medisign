# Generated by Django 4.2.4 on 2023-08-14 15:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("medicines", "0011_alter_medicine_image_alter_prescription_dosage_times_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prescription",
            name="dosage_times",
            field=models.ManyToManyField(blank=True, to="medicines.dosagetime"),
        ),
    ]