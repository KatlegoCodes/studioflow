from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required
from django.contrib import messages

from .models import Client
from .forms import ClientForm

@login_required
@admin_required
def client_list(request):
    clients = Client.objects.all().order_by('-created_at')
    return render(request, 'clients/client_list.html', {'clients': clients})

@login_required
@admin_required
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.created_by = request.user
            client.save()
            messages.success(request, 'Client created successfully!')
            return redirect('client_list')
        else:
            
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ClientForm()
        

    return render(request, 'clients/client_form.html', {'form': form}) 

@login_required
@admin_required
def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'clients/client_detail.html', {'client': client})

@login_required
@admin_required
def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client updated successfully!')
            return redirect('client_detail', pk=client.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ClientForm(instance=client)

    return render(request, 'clients/client_form.html', {'form': form})

@login_required
@admin_required
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)

    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Client deleted successfully!')
        return redirect('client_list')
    
    return render(request, 'clients/client_confirm.html', {'client': client})