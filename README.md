# 🧾 Invoice Management System

A professional Django-based invoicing system for tracking client invoices, projects, and payments.

## 🚀 Features

- ✅ **Client & Project Management** - Link invoices to clients and projects
- ✅ **Invoice Lifecycle** - Draft → Sent → Paid/Overdue status tracking
- ✅ **Auto-timestamping** - Automatic creation dates for invoices
- ✅ **Foreign Key Relationships** - Clean data structure with CASCADE deletes
- ✅ **Admin Interface** - Built-in Django admin for easy management

## 📋 Database Schema

### Invoice Model
```python
class Invoice(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('sent', 'Sent'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue')
    )
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    due_date = models.DateField()
    date_by = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Invoice {self.id}"
