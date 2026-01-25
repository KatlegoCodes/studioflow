from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Project
from .forms import ProjectForm
from accounts.decorators import admin_required

@login_required
def project_list(request):
    projects = Project.objects.select_related('client').all()
    return render(request, 'projects/project_list.html', {
        'projects': projects
    })

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {
        'project': project
    })

@admin_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(project_list)
    else:
        form = ProjectForm()
    
    return render(request, 'projects/project_form.html', {
        'form': form,
        'title': 'New Project'
    })

@admin_required
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)

    return redirect(request, 'projects/projects_form.html', {
        'form': form,
        'title': 'Edit Project'
    })

@admin_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        project.delete()
        return redirect(request, 'projects/project_delete.html', {
            'project': project
        })