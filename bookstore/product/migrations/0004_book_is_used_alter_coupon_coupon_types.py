# Generated by Django 5.0.3 on 2024-03-26 10:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_coupon"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="is_used",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="coupon",
            name="coupon_types",
            field=models.CharField(
                choices=[
                    ("Percentage Discount", "Percentage Discount"),
                    ("Flat Discount", "Flat Discount"),
                    ("Bulk Discount", "Bulk Discount"),
                    ("Free Shipping", "Free Shipping"),
                ],
                default="Percentage Discount",
                max_length=400,
            ),
        ),
    ]
