from django.db import models
import uuid
from django.core.validators import MinValueValidator
from decimal import Decimal

# Model for data storage. 
class ReceiptData(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    points = models.IntegerField(null=False)