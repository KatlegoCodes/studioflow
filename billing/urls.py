from django.urls import path
from . import views

urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('new/', views.invoice_create, name='invoice_create'),
    path('<int:pk>/edit', views.invoice_update, name='invoice_update'),
    path('invoices/<int:pk>/delete', views.invoice_delete, name='invoice_delete'),
    path('<int:pk>/mark-paid/', views.invoice_mark_paid, name='invoice_mark_paid'),
    path('invoice/<int:pk>/print/', views.invoice_print, name='invoice_print'),
]