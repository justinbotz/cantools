# users/urls.py
from django.urls import path
from . import views
from .views import newasset,edit_asset,asset_detail, add_to_wishlist,toggle_request_asset, checkout_requested_assets





urlpatterns = [

    path("newasset", newasset, name="newasset"),
    path("editasset/", edit_asset, name="edit_asset"),
    path('asset/<int:asset_id>/', asset_detail, name='asset_detail'),
    path('asset/toggle_request/<int:asset_id>/<int:library_id>/', toggle_request_asset, name='toggle_request_asset'),
    path('asset/checkout_requested/', checkout_requested_assets, name='checkout_requested_assets'),
    path('asset/checkout/<int:asset_id>/', views.checkout_asset, name='checkout_asset'),
    path('wishlist/add/<int:asset_id>/', add_to_wishlist, name='add_to_wishlist'),

]