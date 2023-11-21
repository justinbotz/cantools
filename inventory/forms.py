from django.forms import ModelForm
from inventory.models import Asset

# Create the form class.
class newassetform(ModelForm):
     class Meta:
          model = Asset
          fields = "Name", "Brand","quantity", "serial", "assettag", "description", "keywords", "condition", "pricepaid", "care", "image", "StreetAddress", "City", "State", "areacode", "checkedout","notes"





