from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from typing import Any
from .models import BooksBook
from .serializers import BookSerializer


class BooksView(generics.ListAPIView):
    queryset = BooksBook.objects.all()
    serializer_class = BookSerializer
