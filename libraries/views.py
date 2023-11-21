from django.shortcuts import get_object_or_404, render, redirect
from .forms import newlibraryform
from .models import LibraryProfile
from inventory.models import  Asset
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


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
    form = newlibraryform()
    context = {'form': form}
    return render(request, 'libraries/newlibrary.html', context)

def edit_library(request, LibraryProfile_id):
    library = get_object_or_404(LibraryProfile, pk=libraryProfile_id, created_by=request.user)  # or however you track the creator
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
    assets = Asset.objects.filter(libraries=library_profile)  # Assuming 'libraries' is the M2M field
    is_following = request.user.is_authenticated and library_profile.followers.filter(id=request.user.id).exists()
    # Pagination
    paginator = Paginator(assets, 10)  # Show 10 assets per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'libraries/library_detail.html', {
        'library': library_profile,  # You can keep this as 'library' in the context for simplicity
        'assets': assets,
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


