from django.db import models
import uuid

# Create your models here.
class Receipt(models.Model):
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)
    points = models.IntegerField(null=False)
    
    def __str__(self):
        return f"ID: {self.id}  ->  Points: {self.points}"