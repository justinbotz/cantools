from django.db import models

# Create your models here.
# In cart/models.py
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assets = models.ManyToManyField(Asset)

# In cart/views.py
# Views to add/remove assets to/from the cart