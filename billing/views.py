from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required

from .models import Invoice
from .forms import InvoiceForm

@login_required
def invoice_list(request):
    invoices = Invoice.objects.select_related('client', 'project').order_by('-created_at')
    return render(request, 'billing/invoice_list.html', {
        'invoices': invoices
    })

@login_required
def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'billing/invoice_detail.html', {
        'invoice': invoice
    })

@admin_required
def invoice_create(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
        
    else:
        form = InvoiceForm

    return render(request, 'billing/invoice_form.html', {
        'form': form,
        'title': 'New Invoice'
    })

@admin_required
def invoice_update(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)

    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_detail', pk=invoice.pk)
    else:
        form = InvoiceForm(instance=invoice)

    return render(request, 'billing/invoice_form.html', {
        'form': form,
        'title': 'Edit Invoice'
    })

@login_required
def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)

    if request.method == 'POST':
        invoice.delete()
        return redirect('invoice_list')
    
    return render(request, 'billing/invoice_confirm_delete.html', {
        'invoice': invoice
    })
