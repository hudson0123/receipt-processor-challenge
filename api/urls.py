from django.urls import path
from .views import CreateReceipt

urlpatterns = [
    path('/receipts/process', CreateReceipt.as_view(), name="create_receipt")
]
