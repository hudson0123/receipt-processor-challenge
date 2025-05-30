from django.db import models
import uuid
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.
class ReceiptData(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    points = models.IntegerField(null=False)
    retailer = models.CharField()
    purchaseDate = models.CharField()
    purchaseTime = models.CharField()
    total = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('0.01'))])
    
class Item(models.Model):
    receipt = models.ForeignKey(ReceiptData, on_delete=models.CASCADE, related_name="items")
    shortDescription = models.CharField()
    price = models.DecimalField(decimal_places=2, max_digits=10, validators=[MinValueValidator(Decimal('0.01'))])