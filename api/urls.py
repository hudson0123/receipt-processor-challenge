from django.urls import path
from .views import CreateReceipt, RetrieveReceipt

# Register the endpoints.
urlpatterns = [
    path('receipts/process', CreateReceipt, name="create_receipt"),
    path('receipts/<uuid:pk>/points', RetrieveReceipt, name="create_receipt"),
]
