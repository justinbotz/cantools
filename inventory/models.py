from django.db import models
from django.contrib.auth.models import User
from libraries.models import LibraryProfile
# Create your models here.
class Asset(models.Model):

    CONDITION = (
        ('n', 'New'),
        ('g', 'Good'),
        ('u', 'Used'),
        ('b', 'Broken'),
    )

    Name = models.CharField(max_length=255, null=True, blank=True)
    Brand = models.CharField(max_length=255, null=True, blank=True)
    quantity = models.IntegerField(default = 1,blank=True, null=True)
    serial = models.CharField(max_length=1000, null=True)
    assettag = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    components=models.CharField(max_length=250, null=True, blank=True)
    condition =models.CharField(max_length=1, choices=CONDITION)
    pricepaid = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    care =models.TextField(blank=True, null=True)
    image=models.ImageField(null= True,blank=True,upload_to='images/')
    StreetAddress = models.CharField(max_length=255, null=True, blank=True)
    City = models.CharField(max_length=50, null=True, blank=True)
    State = models.CharField(max_length=50, null=True, blank=True)
    areacode = models.IntegerField(blank=True, null=True)
    checkedout = models.BooleanField(default=False)
    requested_by = models.ManyToManyField(User, related_name='requested_assets', blank=True)
    checked_out_by = models.ForeignKey(User, related_name='checked_out_assets', on_delete=models.SET_NULL, null=True,
                                       blank=True)
    timestamp= models.DateTimeField(auto_now_add=True,blank=True)
    notes=models.TextField(blank=True, null=True)
    ordering = ['id']
    libraries = models.ManyToManyField(LibraryProfile)



    def _str_(self):
        return self.Name