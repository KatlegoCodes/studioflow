from django.contrib.auth.models import User
from django.db import models
from clients.models import Client

class Project(models.Model):
    STATUS_ChOICES = (
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
    )

    name = models.CharField(max_length=255)
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='projects'
    )

    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_ChOICES,
        default='pending'
    )

    start_date = models.DateField()
    due_date = models.DateField()

    assigned_staff = models.ManyToManyField(
        User,
        blank=True,
        related_name='assigned_projects'
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_projects'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
