# Generated by Django 4.2.7 on 2023-11-20 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0004_asset_checked_out_by_asset_requested_by_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Wishlist",
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
                ("assets", models.ManyToManyField(blank=True, to="inventory.asset")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wishlist",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
