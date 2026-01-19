from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'project', 'amount', 'status', 'due_date')
    list_filter = ('status')
    search_fields = ('client__name', 'project__name')