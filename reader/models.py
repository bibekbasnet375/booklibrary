from django.db import models
import math
from datetime import timedelta
from django.utils import timezone

class BookReader(models.Model):
    book = models.ForeignKey("books.Books", on_delete=models.CASCADE)
    reader = models.ForeignKey("reader.Reader", on_delete=models.CASCADE)
    due_date = models.DateField(default=timezone.now)

    def get_remaining_days(self):
        due_date = self.due_date
        now = timezone.now()
        return math.floor(timedelta(now-due_date)/86400)

class Reader(models.Model):
    Full_name= models.CharField(max_length=50)
    Email= models.EmailField(unique=True)
    Address= models.CharField()
    contact_no= models.BigIntegerField()

    def __str__(self):
        return self.Full_name


