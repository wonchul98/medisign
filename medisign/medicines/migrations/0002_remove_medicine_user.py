# Generated by Django 4.2.4 on 2023-08-03 17:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("medicines", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="medicine",
            name="user",
        ),
    ]
