# Generated by Django 4.2.4 on 2023-08-24 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("medicines", "0023_medicineimage"),
    ]

    operations = [
        migrations.AddField(
            model_name="medicineimage",
            name="Prescription",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="medicineImages",
                to="medicines.prescription",
            ),
        ),
    ]
