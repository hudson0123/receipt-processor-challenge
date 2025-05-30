from django.shortcuts import render
from rest_framework import generics
from .models import ReceiptData
from .serializers import ReceiptDataSerializer

# Create your views here.
class CreateReceipt(generics.CreateAPIView):
    queryset = ReceiptData.objects.all()
    serializer_class = ReceiptDataSerializer
    
    def perform_create(self, serializer): 
        print(serializer.validated_data)
        instance = serializer.save(points=5)
    
class RetrieveReceipt(generics.RetrieveAPIView):
    queryset = ReceiptData.objects.all()
    serializer_class = ReceiptDataSerializer