# Generated by Django 4.1.7 on 2023-03-13 17:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("car_id", models.IntegerField()),
                ("customer_need", models.CharField(max_length=100)),
                ("car_title", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.IntegerField()),
                ("message", models.TextField(blank=True)),
                ("user_id", models.IntegerField(blank=True)),
                (
                    "create_date",
                    models.DateTimeField(default=datetime.datetime.now, max_length=100),
                ),
            ],
        ),
    ]
