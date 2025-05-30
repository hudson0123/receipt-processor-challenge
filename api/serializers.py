from rest_framework import serializers
from .models import ReceiptData, Item

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = (
            "shortDescription",
            "price"
        )

class ReceiptDataSerializer(serializers.ModelSerializer):
    
    items = ItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = ReceiptData
        fields = (
            "id",
            "points",
            "retailer",
            "purchaseDate",
            "purchaseTime",
            "total",
            "items",
        )
        
        extra_kwargs = {
            "points": {"read_only": True}
        }

