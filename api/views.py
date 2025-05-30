from django.shortcuts import render
from rest_framework import generics
from .models import Receipt
from .serializers import ReceiptSerializer

# Create your views here.
class CreateReceipt(generics.CreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer