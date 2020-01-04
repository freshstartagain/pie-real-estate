from rest_framework import serializers

from listings.serializers import ListingSerializer
from .models import Realtor


class RealtorSerializer(serializers.ModelSerializer):
    listings = ListingSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Realtor
        fields = "__all__"
