# Generated by Django 4.2.4 on 2023-08-18 09:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0008_alter_user_regular_pharmacy"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="widget",
            field=models.TextField(blank=True),
        ),
    ]