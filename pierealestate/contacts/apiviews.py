from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Contact
from .serializers import ContactSerializer

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetail(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer