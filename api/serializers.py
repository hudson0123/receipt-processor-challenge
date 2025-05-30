from rest_framework import serializers
from .models import ReceiptData

# This will serialize the data for incoming and outgoing api data.
class ReceiptDataSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = ReceiptData
        fields = (
            "id",
            "points",
        )
        
        extra_kwargs = {
            "points": {"read_only": True},
        }