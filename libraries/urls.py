from django.urls import path
from .views import newlibrary, edit_library,library_detail,library_list, follow_library, unfollow_library,library_admin


urlpatterns = [

    path("", newlibrary, name="new_library"),
    path("editlibrary/", edit_library, name="edit_Library"),
    path('library/<int:libraryprofile_id>/', library_detail, name='library_detail'),

    path('libraries/', library_list, name='library_list'),
    path('library/follow/<int:library_id>/', follow_library, name='follow_library'),
    path('library/unfollow/<int:library_id>/', unfollow_library, name='unfollow_library'),
    path('library/<int:library_id>/libadmin/', library_admin, name='library_admin'),


]