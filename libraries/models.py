from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

from django.db.models.signals import post_save
class LibraryProfile(models.Model):
    # Basic Library Information
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    followers = models.ManyToManyField(User, related_name='followed_libraries', blank=True)

    # Images
    profile_picture = models.ImageField(upload_to='library_profiles/',blank=True)
    header_image = models.ImageField(upload_to='library_profiles/',blank=True)

    # Address Information
    street_address = models.CharField(max_length=255,blank=True)
    city = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    zip_code = models.CharField(max_length=20,blank=True)

    # FAQs and Contact
    faqs = models.TextField(help_text="Frequently Asked Questions",blank=True)
    contact = models.TextField(help_text="Contact Information",blank=True)

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

class LibraryVisit(models.Model):
    library = models.ForeignKey(LibraryProfile, on_delete=models.CASCADE, related_name="visits")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} visited {self.library.name} on {self.visit_date}"