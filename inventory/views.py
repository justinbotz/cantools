from django.shortcuts import render, get_object_or_404, redirect
from .forms import newassetform
from .models import Asset
from users.models import Wishlist
from django.contrib.auth.decorators import login_required

# Create your views here.
def newasset(request):
    form = newassetform()
    context = {'form': form}
    return render(request, 'inventory/newasset.html', context)

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
def request_asset(request, asset_id):
    asset = get_object_or_404(Asset, pk=asset_id)
    asset.requested_by.add(request.user)
    # Additional logic to notify the user when the asset becomes available, etc.
    return redirect('asset_detail', asset_id=asset_id)

@login_required
def checkout_asset(request, asset_id):
    asset = get_object_or_404(Asset, pk=asset_id)
    if request.user in asset.requested_by.all():
        asset.checked_out = True
        asset.checked_out_by = request.user
        asset.save()
        # Additional logic for checkout process
    return redirect('asset_detail', asset_id=asset_id)

def add_to_wishlist(request, asset_id):
    asset = get_object_or_404(Asset, pk=asset_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.assets.add(asset)
    # Redirect to some page
    return redirect('some_view')
