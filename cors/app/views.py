import uuid

from django.middleware.csrf import get_token
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book
from .serializers import BookSerializer


# Create your views here.
class BooksView(APIView):
    @staticmethod
    def get(request: Request):
        books = Book.objects.order_by('pub_date')
        serializer = BookSerializer(books, many=True)
        return Response({'msg': 'ok', 'data': serializer.data})

    @staticmethod
    def post(request: Request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'ok', 'data': serializer.data})
        return Response({'msg': 'fail', 'data': serializer.errors})


class BooksView2(APIView):
    @staticmethod
    def get(request: Request):
        books = Book.objects.order_by('pub_date')
        serializer = BookSerializer(books, many=True)
        return Response({'msg': 'ok', 'data': serializer.data})


class BookView(APIView):
    @staticmethod
    def get(request, pk):
        book = Book.objects.get(id=pk)
        return Response({'msg': 'ok', 'data': BookSerializer(book).data})

    @staticmethod
    def put(request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'ok', 'data': serializer.data})
        return Response({'msg': 'fail', 'data': serializer.errors})

    @staticmethod
    def delete(request, pk):
        Book.objects.filter(id=pk).delete()
        return Response({"msg": 'ok'})
