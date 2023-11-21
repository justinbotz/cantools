from django.shortcuts import render

# Create your views here.
# users/views.py
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from users.forms import CustomUserCreationForm, UserProfileForm

def dashboard(request):
    return render(request, "users/dashboard.html")
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
