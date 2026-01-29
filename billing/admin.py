from django.contrib import admin
from .models import Invoice, InvoiceItem

class InvoiceItemline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'project','status', 'due_date')
    list_filter = ('status',)
    search_fields = ('client__name', 'project__name')
    inlines = [InvoiceItemline]

@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('description', 'invoice', 'quantity', 'unit_price')