from django.forms import ModelForm
from libraries.models import LibraryProfile

# Create the form class.
class newlibraryform(ModelForm):
     class Meta:
          model = LibraryProfile
          fields = "__all__"



