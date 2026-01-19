from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'status', 'start_date', 'due_date')
    list_filter = ('status', 'client')
    search_fields = ('name', 'client__name')
    filter_horizontal = ('assigned_staff',)