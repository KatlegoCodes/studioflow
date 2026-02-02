from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required
from django.contrib import messages

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

    if invoice.status == 'paid':
        messages.error(request, 'Paid invoices cannot be edited')
        return redirect('invoice_detail', pk=pk)
    
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to edit invoices')
        return redirect('invoice_detail', pk=pk)
    
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            messages.success(request, 'Invoice updated')
            return redirect('invoice_detail', pk=pk)
    else:
        form = InvoiceForm(instance=invoice)

    return render(request, 'billing/invoice_form.html', {'form': form})


@login_required
def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)

    if invoice.status == 'paid':
        messages.error(request, 'Paid invoices cannot be deleted')
        return redirect('invoice_detail', pk=pk)
    
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to delete invoices')
        return redirect('invoice_detail', pk=pk)

    if request.method == 'POST':
        invoice.delete()
        messages.success(request, 'Invoice deleted')
        return redirect('invoice_list')
    
    return render(request, 'billing/invoice_confirm_delete.html', {
        'invoice': invoice
    })

    

@login_required
def invoice_mark_paid(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)

    if not request.user.is_staff:
        messages.error(request,'You do not have permission to mark invoices as paid')
        return redirect('invoice_detail', pk=pk)
    
    if invoice.status == 'paid':
        messages.info(request, 'Invoice is already marked as paid.')
        return redirect('invoice_detail', pk=pk)
    
    invoice.status = 'paid'
    invoice.save()

    messages.success(request, 'Invoice marked as paid')
    return redirect('invoice_detail', pk=pk)

@login_required
@admin_required
def invoice_print(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'billing/invoice_print.html', {'invoice': invoice})