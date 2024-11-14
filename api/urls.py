from django.urls import path
from .views import InvoiceView

urlpatterns = [
    path('invoices/', InvoiceView.as_view(), name='invoice-list'),
    path('invoices/<str:invoice_number>/', InvoiceView.as_view(), name='invoice-detail'),
]
