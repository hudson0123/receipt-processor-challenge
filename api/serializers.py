from rest_framework import serializers
from .models import ReceiptData, Item

class ReceiptDataSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = ReceiptData
        fields = (
            "id",
            "points",
            "retailer",
            "purchaseDate",
            "purchaseTime",
            "total",
        )
        
        extra_kwargs = {
            "points": {"read_only": True},

        }

