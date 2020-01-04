from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Listing
from .serializers import ListingSerializer

class ListingList(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

class ListingDetail(generics.RetrieveAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer