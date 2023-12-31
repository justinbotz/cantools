# Generated by Django 4.2.7 on 2023-12-15 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="LibraryProfile",
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
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True)),
                (
                    "profile_picture",
                    models.ImageField(blank=True, upload_to="library_profiles/"),
                ),
                (
                    "header_image",
                    models.ImageField(blank=True, upload_to="library_profiles/"),
                ),
                ("street_address", models.CharField(blank=True, max_length=255)),
                ("city", models.CharField(blank=True, max_length=100)),
                ("state", models.CharField(blank=True, max_length=100)),
                ("zip_code", models.CharField(blank=True, max_length=20)),
                (
                    "faqs",
                    models.TextField(
                        blank=True, help_text="Frequently Asked Questions"
                    ),
                ),
                (
                    "contact",
                    models.TextField(blank=True, help_text="Contact Information"),
                ),
                ("opening_hours", models.CharField(blank=True, max_length=255)),
                ("website_url", models.URLField(blank=True)),
                ("facebook_url", models.URLField(blank=True)),
                ("twitter_url", models.URLField(blank=True)),
                ("instagram_url", models.URLField(blank=True)),
                ("accessibility_info", models.TextField(blank=True)),
                ("membership_info", models.TextField(blank=True)),
                ("catalog_link", models.URLField(blank=True)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
                ("unique_features", models.TextField(blank=True)),
                ("contact_email", models.EmailField(blank=True, max_length=254)),
                ("contact_phone", models.CharField(blank=True, max_length=20)),
                ("collection_size", models.IntegerField(blank=True, null=True)),
                ("languages_supported", models.CharField(blank=True, max_length=255)),
                ("public_transport_links", models.TextField(blank=True)),
                (
                    "followers",
                    models.ManyToManyField(
                        blank=True,
                        related_name="followed_libraries",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LibraryVisit",
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
                ("visit_date", models.DateTimeField(auto_now_add=True)),
                (
                    "library",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="visits",
                        to="libraries.libraryprofile",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
