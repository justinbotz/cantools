
from django.forms import ModelForm
from .models import LibraryProfile

# Create the form class.
class newlibraryform(ModelForm):
     class Meta:
          model = LibraryProfile
          fields = "name","description","profile_picture","contact_email","contact_phone", "street_address","city","state","zip_code"



