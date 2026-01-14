from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from reader.models import Reader
from drf_yasg.utils import swagger_auto_schema
from reader.serializers import ReaderSerializer
from django.shortcuts import get_object_or_404


class Readerlist(APIView):

    @swagger_auto_schema(responses={200: ReaderSerializer(many=True)})
    def get(self, request, format=None):
        r= Reader.objects.all()
        serializer= ReaderSerializer(r, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body= ReaderSerializer)
    def post(self, request, format=None):
        serializer= ReaderSerializer(data=request.data)
        if serializer .is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReaderDetail(APIView):
    
    @swagger_auto_schema(request_body=ReaderSerializer)
    def put(self, request, pk, format=None):
        Reader = self.get_object(pk)
        serializer = ReaderSerializer(Reader, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(responses={204: 'Deleted'}) 
    def delete(self, request, pk, format=None):
        Reader = get_object_or_404(Reader, pk=pk)
        Reader.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)