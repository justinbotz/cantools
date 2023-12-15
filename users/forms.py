from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("username","first_name","last_name","email",)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "profile_picture","header_image","street_address","city","state","zip_code","email","phone_number"