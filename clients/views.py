from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import admin_required

@login_required
@admin_required
def client_create(request):
    return render(request, 'client/client_form.html')
