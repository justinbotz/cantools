from django.shortcuts import render

# Create your views here.
# users/views.py
from django.contrib.auth import login
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from users.forms import CustomUserCreationForm, UserProfileForm
from libraries.models import LibraryProfile, LibraryVisit
from libraries.urls import follow_library, unfollow_library
from django.core.paginator import Paginator

from inventory.models import Asset
from django.contrib.auth.decorators import login_required



def dashboard(request):


    if request.user.is_authenticated:
            followed_libraries = LibraryProfile.objects.filter(followers=request.user)
            libraries = LibraryProfile.objects.all()
            paginator = Paginator(libraries, 10)  # Show 10 assets per page
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
    else:
            followed_libraries = LibraryProfile.objects.none()
            libraries = LibraryProfile.objects.none()
            paginator = Paginator(libraries, 10)  # Show 10 assets per page
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)


    return render(request, "users/dashboard.html", {
                'followed_libraries': followed_libraries,
                'page_obj': page_obj,
                'page_number': page_number,
                'libraries': libraries
            })


def register(request):
    if request.method =="GET":
        return render(
            request, "registration/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect(reverse("dashboard"))



def edituserprofile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to a success page
    else:
        form = UserProfileForm(instance=request.user.userprofile)

    return render(request, 'users/edituserprofile.html', {'form': form})
