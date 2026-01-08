from django.db import models

class Books(models.Model):
    Title= models.CharField(max_length=60)
    Published_date= models.DateField()
    Author= models.CharField(max_length=50)
    ISBN= models.IntegerField()
    Stock= models.IntegerField()

    def __str__(self):
        return self.Title

