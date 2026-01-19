from django.db import models
from clients.models import Client
from projects.models import Project

class Invoice(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue')
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    due_date = models.DateField()
    date_by = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice {self.id}"