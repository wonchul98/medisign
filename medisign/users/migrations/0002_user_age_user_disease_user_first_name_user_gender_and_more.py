# Generated by Django 4.2.4 on 2023-08-03 05:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="age",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="disease",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="user",
            name="first_name",
            field=models.CharField(blank=True, max_length=150, verbose_name="first name"),
        ),
        migrations.AddField(
            model_name="user",
            name="gender",
            field=models.CharField(
                blank=True, choices=[("M", "Male"), ("F", "Female"), ("C", "Custom")], max_length=255
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="height",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="last_name",
            field=models.CharField(blank=True, max_length=150, verbose_name="last name"),
        ),
        migrations.AddField(
            model_name="user",
            name="medicine",
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="user",
            name="profile_photo",
            field=models.ImageField(blank=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="user",
            name="user_name",
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name="user",
            name="weight",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
