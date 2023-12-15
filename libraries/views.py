from django.shortcuts import get_object_or_404, render, redirect
from .forms import newlibraryform
from .models import LibraryProfile, LibraryVisit
from django.db.models.functions import TruncMonth
from django.db.models import Count
from inventory.models import  Asset, AssetRequest
from users.models import User, UserProfile
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse


from collections import OrderedDict
import csv



# Create your views here.

@login_required
def follow_library(request, library_id):
    library = get_object_or_404(LibraryProfile, pk=library_id)
    library.followers.add(request.user)
    return HttpResponseRedirect(reverse('library_list'))  # Redirect to the library list

@login_required
def unfollow_library(request, library_id):
    library = get_object_or_404(LibraryProfile, pk=library_id)
    library.followers.remove(request.user)
    return HttpResponseRedirect(reverse('library_list'))


def newlibrary(request):
    if request.method == 'POST':
        form = newlibraryform(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # Process the data in form.cleaned_data
            # e.g., form.save() if it's a ModelForm
            return redirect('new_library')  # Redirect after POST
    else:
        form = newlibraryform()  # Provide an empty form for GET request

    # Render the form with context
    return render(request, 'libraries/newlibrary.html', {'form': form})

def edit_library(request, library_id):
    library = get_object_or_404(LibraryProfile, pk=library_id, created_by=request.user)  # or however you track the creator
    if request.method == 'POST':
        form = newlibraryform(request.POST, instance=library)
        if form.is_valid():
            form.save()
            return redirect('some_success_url')
    else:
        form = newlibraryform(instance=library)

    return render(request, 'edit_library.html', {'form': form})

def library_detail(request, libraryprofile_id):
    library_profile = get_object_or_404(LibraryProfile, pk=libraryprofile_id)
    # Record the visit
    if request.user.is_authenticated:
        LibraryVisit.objects.create(library=library_profile, user=request.user)
    assets = Asset.objects.filter(libraries=library_profile)  # Assuming 'libraries' is the M2M field
    is_following = request.user.is_authenticated and library_profile.followers.filter(id=request.user.id).exists()
    user_requested_assets = Asset.objects.filter(libraries=library_profile, requested_by=request.user)
    user_checked_out_assets = Asset.objects.filter(libraries=library_profile, checked_out_by=request.user)
    # Pagination
    paginator = Paginator(assets, 10)  # Show 10 assets per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'libraries/library_detail.html',{
        'library': library_profile,  # You can keep this as 'library' in the context for simplicity
        'assets': assets,
        'user_requested_assets': user_requested_assets,
        'user_checked_out_assets': user_checked_out_assets,
        'page_obj': page_obj,
        'is_following': is_following,
    })

def dashboard(request):
    return render(request, "base.html")

def library_list(request):
    libraries = LibraryProfile.objects.all()
    paginator = Paginator(libraries, 10)  # Show 10 assets per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # Query to get all libraries
    return render(request, 'libraries/library_list.html', {
        'libraries': libraries,
        'page_obj': page_obj,
    })




def library_admin(request, library_id):  # Add library_id as a parameter
    library_profile = get_object_or_404(LibraryProfile, pk=library_id)

    try:
        library = LibraryProfile.objects.get(id=library_id)
    except LibraryProfile.DoesNotExist:
        # Handle the case where the library does not exist
        pass
    # User Info logic

    followers = library_profile.followers.all()  # This gives you a queryset of User objects

    follower_details = []
    for user in followers:
        user_profile = UserProfile.objects.get(user=user)
        checked_out_assets = Asset.objects.filter(checked_out_by=user)  # Modify according to your Asset model

        follower_details.append({
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'status': user_profile.status,
            'date_joined': user_profile.member_since,
            'checked_out_assets': [asset.Name for asset in checked_out_assets],
            # Assuming asset has a 'name' field
        })


    # Assuming 'libraries' is the M2M field
    if request.user.is_authenticated:
        user_requested_assets = Asset.objects.filter(libraries=library_profile, requested_by=request.user)
    else:
        user_requested_assets = Asset.objects.none()  # Return an empty queryset
    assets = Asset.objects.filter(libraries=library_profile)
    user_requested_assets = Asset.objects.filter(libraries=library_profile, requested_by=request.user)
    user_checked_out_assets = Asset.objects.filter(libraries=library_profile, checked_out_by=request.user)

    # Pagination
    paginator = Paginator(assets, 10)  # Show 10 assets per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    user_counts = User.objects.annotate(
        month=TruncMonth('date_joined')
    ).values('month').annotate(
        count=Count('id')
    ).order_by('month')

    # Convert QuerySet to a format suitable for Chart.js
    chart_data = {
        'labels': [item['month'].strftime("%Y-%m") for item in user_counts],
        'data': [item['count'] for item in user_counts],
    }

    asset_counts = Asset.objects.annotate(
        month=TruncMonth('timestamp')
    ).values('month').annotate(
        count=Count('id')
    ).order_by('month')

    asset_chart_data = {
        'labels': [item['month'].strftime("%Y-%m") for item in asset_counts],
        'data': [item['count'] for item in asset_counts],
    }

    # Asset count code

    # Example for requested items (adjust as per your requirement)
    requested_counts = AssetRequest.objects.annotate(
        month=TruncMonth('date_requested')  # Assuming 'date_requested' is the field name
    ).values('month').annotate(
        count=Count('id')
    ).order_by('month')

    requested_chart_data = {
        'labels': [item['month'].strftime("%Y-%m") for item in requested_counts],
        'data': [item['count'] for item in requested_counts],
    }


    # Example for requested items
    requested_counts = Asset.objects.annotate(
        month=TruncMonth('timestamp')
    ).values('month', 'Name').annotate(
        count=Count('id')
    ).order_by('month', '-count')  # Adjust based on your models and fields

    visit_counts = LibraryVisit.objects.annotate(
        month=TruncMonth('visit_date')  # Replace 'visit_date' with your actual field name
    ).values('month').annotate(
        count=Count('id')
    ).order_by('month')

    visit_chart_data = {
        'labels': [item['month'].strftime("%Y-%m") for item in visit_counts],
        'data': [item['count'] for item in visit_counts],
    }

    return render(request, 'libraries/lib_admin.html', {
        'library': library,
        'follower_details': follower_details,
        'assets': assets,
        'user_requested_assets': user_requested_assets,
        'user_checked_out_assets':user_checked_out_assets,
        # ... other context variables ...
        'asset_chart_data': asset_chart_data,
        'requested_chart_data': requested_chart_data, # Ensure this is defined as per your data
        'visit_chart_data': visit_chart_data,
        'chart_data': chart_data,
        'requested_counts': requested_counts,
        'page_obj': page_obj,
        'UserProfile': UserProfile
    })