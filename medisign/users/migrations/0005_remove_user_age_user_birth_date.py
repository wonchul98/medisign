# Generated by Django 4.2.4 on 2023-08-05 10:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_user_disease_alter_user_medicine"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="age",
        ),
        migrations.AddField(
            model_name="user",
            name="birth_date",
            field=models.DateField(null=True),
        ),
    ]
