from django.db import models
from datetime import datetime
# Create your models here.

class Invoice(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    quantity = models.IntegerField()
    sub_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    order_date = models.DateTimeField(default=datetime.now, blank=True)
