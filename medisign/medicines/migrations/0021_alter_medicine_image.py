# Generated by Django 4.2.4 on 2023-08-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("medicines", "0020_contraindication_detail"),
    ]

    operations = [
        migrations.AlterField(
            model_name="medicine",
            name="image",
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]