from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Realtor
from .serializers import RealtorSerializer


class RealtorList(generics.ListAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer

class RealtorDetail(generics.RetrieveAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer