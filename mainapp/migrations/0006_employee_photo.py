# Generated by Django 4.1 on 2025-01-29 09:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0005_indianrestaurantitem_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="restaurant/items/"
            ),
        ),
    ]
