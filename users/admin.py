from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import UserProfile
from django.contrib.auth.models import User, Group
from libraries.models import LibraryProfile

class FollowedLibrariesInline(admin.TabularInline):
    model = LibraryProfile.followers.through
    verbose_name = "Followed Library"
    verbose_name_plural = "Followed Libraries"
    extra = 1  # Number of extra forms to display

class ProfileInline(admin.StackedInline):
    model = UserProfile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline,(FollowedLibrariesInline)]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
# Remove: admin.site.register(Profile)'first_name', 'last_name')