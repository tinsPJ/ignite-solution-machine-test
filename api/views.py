from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from typing import Any
from .models import (
    BooksBook,
    BooksLanguage,
    BooksAuthor,
    BooksFormat,
    BooksSubject,
    BooksBookshelf,
)
from .serializers import BookSerializer
from django.db.models import Q


class BooksView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        """
        Search/ Filtration by
        Book ID numbers specified as Project Gutenberg ID numbers.
        Language,Mime-type,Topic,Author and title.
        """
        queryset = (
            BooksBook.objects.prefetch_related("format")
            .prefetch_related("author")
            .prefetch_related("language")
            .prefetch_related("subject")
            .prefetch_related("shelf")
            .all()
        )
        search_query = []
        book_id = self.request.query_params.get("book_id", None)
        lang = self.request.query_params.get("lang", None)
        author = self.request.query_params.get("author", None)
        title = self.request.query_params.get("title", None)
        mime_type = self.request.query_params.get("mime_type", None)
        topic = self.request.query_params.get("topic", None)
        if book_id:
            search_query.append(Q(gutenberg_id=book_id))
        if lang:
            language_id = BooksLanguage.objects.filter(code=lang).values_list(
                "id", flat=True
            )
            search_query.append(Q(language__language_id__in=language_id))
        if author:
            author_id = BooksAuthor.objects.filter(name__icontains=author).values_list(
                "id", flat=True
            )
            search_query.append(Q(author__author_id__in=author_id))
        if title:
            search_query.append(Q(title__istartswith=title))
        if mime_type:
            mime_type_id = BooksFormat.objects.filter(
                mime_type__istartswith=mime_type
            ).values_list("book_id", flat=True)
            search_query.append(Q(id__in=mime_type_id))
        if topic:
            subject_id = BooksSubject.objects.filter(
                name__istartswith=topic
            ).values_list("id", flat=True)
            shelf_id = BooksBookshelf.objects.filter(
                name__istartswith=topic
            ).values_list("id", flat=True)
            search_query.append(
                Q(subject__subject_id__in=[subject_id])
                | Q(shelf__bookshelf_id__in=[shelf_id])
            )

        return queryset.filter(*search_query)
