from django.urls import path

from .apiviews import RealtorList, RealtorDetail

urlpatterns = [
    path("", RealtorList.as_view(), name="realtor_list"),
    path("<int:pk>/", RealtorDetail.as_view(), name="realtor_detail"),
]

