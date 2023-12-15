from django.db import models
from django.utils import timezone
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
    ShortDescription = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    components=models.CharField(max_length=250, null=True, blank=True)
    condition =models.CharField(max_length=1, choices=CONDITION)
    pricepaid = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    care =models.TextField(blank=True, null=True)
    image=models.ImageField(null= True,blank=True,upload_to='images/assets/<int:asset_id>')
    StreetAddress = models.CharField(max_length=255, null=True, blank=True)
    City = models.CharField(max_length=50, null=True, blank=True)
    State = models.CharField(max_length=50, null=True, blank=True)
    areacode = models.IntegerField(blank=True, null=True)
    checkedout = models.BooleanField(default=False)
    Requested = models.BooleanField(default=False)
    requested_by = models.ManyToManyField(User, related_name='requested_assets', blank=True)
    checked_out_by = models.ForeignKey(User, related_name='checked_out_assets', on_delete=models.SET_NULL, null=True,
                                       blank=True)
    timestamp= models.DateTimeField(auto_now_add=True,blank=True)
    notes=models.TextField(blank=True, null=True)
    ordering = ['id']
    libraries = models.ManyToManyField(LibraryProfile)



    def _str_(self):
        return self.Name

class AssetRequest(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='requests')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asset_requests')
    date_requested = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Request for {self.asset} on {self.date_requested}"

    class Meta:
        verbose_name = "Asset Request"
        verbose_name_plural = "Asset Requests"
