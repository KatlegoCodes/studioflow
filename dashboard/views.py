from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from clients.models import Client
from projects.models import Project
from billing.models import Invoice


@login_required
def dashboard(request):
    context = {
        'client_count': Client.objects.count(),
        'project_count': Project.objects.count(),
        'recent_projects': Project.objects.select_related('client').order_by('-created_at')[:5],
        'unpaid_invoices': Invoice.objects.filter(
            status__in=['draft', 'sent', 'overdue']
        ).order_by('due_date')[:5]
    }
    return render(request, 'dashboard/dashboard.html', context)
