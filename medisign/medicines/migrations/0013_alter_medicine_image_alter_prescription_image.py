# Generated by Django 4.2.4 on 2023-08-14 15:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("medicines", "0012_alter_prescription_dosage_times"),
    ]

    operations = [
        migrations.AlterField(
            model_name="medicine",
            name="image",
            field=models.ImageField(blank=True, default=None, null=True, upload_to="medicine_pictures/"),
        ),
        migrations.AlterField(
            model_name="prescription",
            name="image",
            field=models.ImageField(blank=True, default=None, null=True, upload_to="prescription_picture/"),
        ),
    ]