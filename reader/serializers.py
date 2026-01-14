from rest_framework import serializers
from reader.models import Reader
from reader.models import Bookborrowed
from rest_framework.response import Response

class BookborrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model= Bookborrowed
        fields= "__all__"

class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Reader
        fields= ["id","Full_name","Email","Address","Book_borrowed","contact_no"]
    Book_borrowed= serializers.SerializerMethodField(method_name="get_book_borrowed")

    def get_book_borrowed(self, obj):
        books= Bookborrowed.objects.filter(reader=obj)
        serializer = BookborrowedSerializer(books, many= True)
        return (serializer.data)