from rest_framework import serializers
from reader.models import Reader
from reader.models import BookReader

class BookreaderSerializer(serializers.ModelSerializer):
    class Meta:
        model= BookReader
        fields= "__all__"

class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Reader
        fields= ["id","Full_name","Email","Address","Book_borrowed","contact_no"]
    Book_borrowed= serializers.SerializerMethodField(method_name="get_book_borrowed")

    def get_book_borrowed(self, request, format=None):
        books= BookReader.objects.all()
        return BookreaderSerializer(books, many= True)