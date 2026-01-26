from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from clients.models import Client
from projects.models import Project


@login_required
def dashboard(request):
    context = {
        'client_count': Client.objects.count(),
        'project_count': Project.objects.count(),
        'recent_projects': Project.objects.select_related('client').order_by('-created_at')[:5],
    }
    return render(request, 'dashboard/dashboard.html', context)
