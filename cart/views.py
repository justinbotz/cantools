from django.shortcuts import render, get_object_or_404, redirect
from .models import Asset
from django.contrib.auth.decorators import login_required



@login_required
def checkout_asset(request, asset_id):
    asset = get_object_or_404(Asset, pk=asset_id)
    # Checkout logic...
    return redirect('some_other_view_name')
from django.shortcuts import render

# Create your views here.
