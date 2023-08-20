# Generated by Django 4.2.4 on 2023-08-20 04:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("medicines", "0014_alter_prescription_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="prescription",
            name="medicine",
        ),
        migrations.AddField(
            model_name="prescription",
            name="medicine",
            field=models.ManyToManyField(blank=True, to="medicines.medicine"),
        ),
    ]
