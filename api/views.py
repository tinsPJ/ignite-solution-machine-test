from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from typing import Any
from .models import BooksBook
from .serializers import BookSerializer


class BooksView(generics.ListAPIView):
    queryset = BooksBook.objects.all().prefetch_related(
        "format").prefetch_related("author").prefetch_related(
            "language").prefetch_related("subject").prefetch_related("shelf")
    serializer_class = BookSerializer
