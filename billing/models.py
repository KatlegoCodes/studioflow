from django.db import models
from clients.models import Client
from projects.models import Project
from django.utils import timezone

class Invoice(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='invoices'
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='invoices'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )

    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_overdue(self):
        return self.status != 'paid' and self.due_date < timezone.now().date()

    def total_amount(self):
        return sum(item.total() for item in self.items.all())

    def __str__(self):
        return f"Invoice {self.id}"


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name='items'
    )
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return self.description

    

    
