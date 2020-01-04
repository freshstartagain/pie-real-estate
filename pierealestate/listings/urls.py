from django.urls import path

from .apiviews import ListingList, ListingDetail


urlpatterns = [
    path("", ListingList.as_view(), name="listing_list"),
    path("<int:pk>/", ListingDetail.as_view(), name="listing_detail")
]