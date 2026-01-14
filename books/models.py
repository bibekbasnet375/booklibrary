from django.db import models
from django.core.exceptions import ValidationError

class Books(models.Model):
    Title= models.CharField(max_length=60)
    Published_date= models.DateField()
    Author= models.CharField(max_length=50)
    ISBN= models.IntegerField()
    Stock= models.PositiveIntegerField(default=0)


    def copies_available(self):
        borrowed_count = self.borrowed_records.filter(returned=False).count()
        return self.Stock - borrowed_count

    def __str__(self):
        return self.Title

""""
    def get_reader_count(self):
        return self.bookreader_set.count()
    
    def get_remaining(self):
        return self.Stock-self.get_reader_count()

    def take_book(self, quantity=1):
        if self.Stock < quantity:
            raise ValidationError("no stock available")
        

        self.stock -= quantity
        self.save(update_fields=["stock"])
        return max(self.stock,0)
"""