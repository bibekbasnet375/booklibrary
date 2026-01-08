from rest_framework import serializers
from books.models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model= Books
        fields= ["id","Title","Published_date","Author","ISBN","Stock"]