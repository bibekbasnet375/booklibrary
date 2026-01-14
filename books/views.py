from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from books.models import Books
from drf_yasg.utils import swagger_auto_schema
from books.serializers import BooksSerializer
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError


class Bookslist(APIView):

    @swagger_auto_schema(responses={200: BooksSerializer(many=True)})
    def get(self, request, format=None):
        books= Books.objects.all()
        serializer= BooksSerializer(books, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body= BooksSerializer)
    def post(self, request, format=None):
        serializer= BooksSerializer(data=request.data)
        if serializer .is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BooksDetail(APIView):

#APIView does not provide get_object(), so we must define it manually when using CBV with APIView.
    def get_object(self, pk):
        return get_object_or_404(Books, pk=pk)
    
    @swagger_auto_schema(request_body=BooksSerializer)
    def put(self, request, pk, format=None):
        books = self.get_object(pk)
        serializer = BooksSerializer(books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'Deleted'}) 
    def delete(self, request, pk, format=None):
        books = get_object_or_404(Books, pk=pk)
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReaderCount(APIView):
     def get_object(self, pk):
        return get_object_or_404(Books, pk=pk)
     
     @swagger_auto_schema(request_body=BooksSerializer)
     def put(self, request, pk, format=None):
        books = self.get_object(pk)
        serializer= BooksSerializer(books, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_404_NOT_FOUND)
        
