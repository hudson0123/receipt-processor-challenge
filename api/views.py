from django.shortcuts import render
from rest_framework import generics
from .models import ReceiptData
from .serializers import ReceiptDataSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import calculate_points

# Create your views here.
@api_view(['POST'])
def CreateReceipt(request):
    print(request.data)
    serializer = ReceiptDataSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save(points=calculate_points(request.data))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def RetrieveReceipt(request, pk):
    
    try:
        receipt = ReceiptData.objects.get(id = pk)
    except ReceiptData.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    serializer = ReceiptDataSerializer(receipt)
    return Response({ "points": serializer.data['points'] })
    