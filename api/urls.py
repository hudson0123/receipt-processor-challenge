from django.urls import path
from .views import CreateReceipt, RetrieveReceipt

urlpatterns = [
    path('receipts/process', CreateReceipt.as_view(), name="create_receipt"),
    path('receipts/<uuid:pk>/points', RetrieveReceipt.as_view(), name="create_receipt"),
]
