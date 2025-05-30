from rest_framework import serializers
from .models import Receipt

class ReceiptSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Receipt
        fields = (
            "id",
            "points",
        )
        
        extra_kwargs = {
            "id": {"read_only": True}
        }