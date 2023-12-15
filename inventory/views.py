from django.shortcuts import render, get_object_or_404, redirect
from .forms import newassetform
from users.models import Wishlist
from django.contrib.auth.decorators import login_required
from .models import Asset
from django.db import transaction
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def newasset(request):
    if request.method =='POST':
        form = newassetform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = newassetform()

    return render(request, 'inventory/newasset.html',{'form': form})


def edit_asset(request, asset_id):
    asset = get_object_or_404(Asset, pk=asset_id, added_by=request.user)  # or however you track the creator
    if request.method == 'POST':
        form = NewAssetForm(request.POST, instance=asset)
        if form.is_valid():
            form.save()
            return redirect('some_success_url')
    else:
        form = NewAssetForm(instance=asset)

    return render(request, 'inventory/editasset.html', {'form': form})


def asset_detail(request, asset_id):
    asset = get_object_or_404(Asset, pk=asset_id)
    return render(request, 'inventory/asset_detail.html', {'asset': asset})





@login_required
def checkout_asset(request, asset_id):
    asset = get_object_or_404(Asset, pk=asset_id)
    if request.user in asset.requested_by.all():
        asset.checked_out = True
        asset.checked_out_by = request.user
        asset.save()
        # Additional logic for checkout process
    return redirect('asset_detail', asset_id=asset_id)

# dwitter/views.py

# ...




def add_to_wishlist(request, asset_id):
    asset = get_object_or_404(Asset, pk=asset_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.assets.add(asset)
    # Redirect to some page
    return redirect('some_view')

@login_required
def toggle_request_asset(request, asset_id, library_id):
    asset = get_object_or_404(Asset, pk=asset_id)
    if request.user in asset.requested_by.all():
        asset.requested_by.remove(request.user)
    else:
        asset.requested_by.add(request.user)

    return redirect('library_detail', libraryprofile_id=library_id)



@login_required
@transaction.atomic
def checkout_requested_assets(request):
    if request.method == 'POST':
        requested_assets = request.user.requested_assets.all()
        for asset in requested_assets:
            asset.checked_out_by = request.user
            asset.checked_out = True
            asset.requested_by.clear()
            asset.save()
        libraryprofile_id = request.POST.get('libraryprofile_id')
        # Redirect to a confirmation page or back to the library
        return redirect('library_detail', libraryprofile_id=libraryprofile_id)
    else:
        # Redirect to some safe page or show an error message
        messages.error(request, "This action is not allowed.")
        return redirect('library_detail')  # Redirect to a safe page where messages can be displayed





