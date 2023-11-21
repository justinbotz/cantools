# Generated by Django 4.2.7 on 2023-11-17 16:37

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
            name="UserProfile",
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
                ("profile_picture", models.ImageField(upload_to="user_profiles/")),
                ("header_image", models.ImageField(upload_to="user_profiles/")),
                ("street_address", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=100)),
                ("state", models.CharField(max_length=100)),
                ("zip_code", models.CharField(max_length=20)),
                ("date_of_birth", models.DateField(blank=True, null=True)),
                ("preferred_pronouns", models.CharField(blank=True, max_length=30)),
                ("phone_number", models.CharField(blank=True, max_length=20)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("personal_website", models.URLField(blank=True)),
                ("biography", models.TextField(blank=True)),
                ("linkedin_url", models.URLField(blank=True)),
                ("facebook_url", models.URLField(blank=True)),
                ("twitter_url", models.URLField(blank=True)),
                ("occupation", models.CharField(blank=True, max_length=100)),
                ("organization", models.CharField(blank=True, max_length=100)),
                ("skills_interests", models.TextField(blank=True)),
                ("country", models.CharField(blank=True, max_length=100)),
                ("region", models.CharField(blank=True, max_length=100)),
                ("preferred_language", models.CharField(blank=True, max_length=30)),
                ("profile_visibility", models.BooleanField(default=True)),
                ("member_since", models.DateTimeField(auto_now_add=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                ("agreed_to_terms", models.BooleanField(default=False)),
                (
                    "follows",
                    models.ManyToManyField(
                        blank=True, related_name="followed_by", to="users.userprofile"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
