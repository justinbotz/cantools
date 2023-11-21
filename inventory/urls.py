# users/urls.py
from django.urls import path
from . import views
from .views import newasset,edit_asset,asset_detail, add_to_wishlist


urlpatterns = [

    path("", newasset, name="new asset"),
    path("editasset/", edit_asset, name="edit_asset"),
    path('asset/<int:asset_id>/', asset_detail, name='asset_detail'),
    path('asset/request/<int:asset_id>/', views.request_asset, name='request_asset'),
    path('asset/checkout/<int:asset_id>/', views.checkout_asset, name='checkout_asset'),
    path('wishlist/add/<int:asset_id>/', add_to_wishlist, name='add_to_wishlist'),
]