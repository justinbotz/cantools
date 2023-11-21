from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
class LibraryProfile(models.Model):
    # Basic Library Information
    name = models.CharField(max_length=200)
    description = models.TextField()

    followers = models.ManyToManyField(User, related_name='followed_libraries', blank=True)

    # Images
    profile_picture = models.ImageField(upload_to='library_profiles/')
    header_image = models.ImageField(upload_to='library_profiles/')

    # Address Information
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    # FAQs and Contact
    faqs = models.TextField(help_text="Frequently Asked Questions")
    contact = models.TextField(help_text="Contact Information")

    # Additional fields
    opening_hours = models.CharField(max_length=255, blank=True)
    website_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    accessibility_info = models.TextField(blank=True)
    membership_info = models.TextField(blank=True)
    catalog_link = models.URLField(blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    unique_features = models.TextField(blank=True)
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    collection_size = models.IntegerField(null=True, blank=True)
    languages_supported = models.CharField(max_length=255, blank=True)
    public_transport_links = models.TextField(blank=True)

    def __str__(self):
        return self.name

