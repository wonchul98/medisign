# Generated by Django 4.2.4 on 2023-08-22 12:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0012_delete_widget"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birth_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]