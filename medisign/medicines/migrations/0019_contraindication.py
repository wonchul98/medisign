# Generated by Django 4.2.4 on 2023-08-22 05:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("medicines", "0018_alter_itemseq_number"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contraindication",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("drugNameA", models.CharField(max_length=255)),
                ("drugNumberA", models.CharField(max_length=100)),
                ("ingredientNameA", models.CharField(max_length=255)),
                ("companyNameA", models.CharField(max_length=255)),
                ("drugNameB", models.CharField(max_length=255)),
                ("drugNumberB", models.CharField(max_length=100)),
                ("ingredientNameB", models.CharField(max_length=255)),
                ("companyNameB", models.CharField(max_length=255)),
            ],
        ),
    ]
