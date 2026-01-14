from django.db import models
import math
from datetime import timedelta
from django.utils import timezone

class Bookborrowed(models.Model):
    book = models.ForeignKey("books.Books", on_delete=models.CASCADE, related_name="borrowed_records")
    reader = models.ForeignKey("reader.Reader", on_delete=models.CASCADE)
    due_date = models.DateField(default=timezone.now)
    returned = models.BooleanField(default=False)

    def remaining_days(self):
        now = timezone.now().date()
        remaining_days= (self.due_date-now).days
        return max(remaining_days, 0)

class Reader(models.Model):
    Full_name= models.CharField(max_length=50)
    Email= models.EmailField(unique=True)
    Address= models.CharField()
    contact_no= models.BigIntegerField()

    def __str__(self):
        return self.Full_name


