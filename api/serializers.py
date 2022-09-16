from rest_framework import serializers
from .models import (
    BooksBook,
    BooksBookAuthors,
    BooksAuthor,
    BooksBookLanguages,
    BooksLanguage,
)


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthor
        fields = "__all__"


class BookLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksLanguage
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksBook
        fields = ("title",)

    def to_representation(self, instance):
        res = super().to_representation(instance)
        # appending author details
        authors = BooksBookAuthors.objects.filter(book_id=instance.id)
        author_objects = [author.author for author in authors]
        res["authors"] = BookAuthorSerializer(author_objects, many=True).data

        # Appending language
        languages = BooksBookLanguages.objects.filter(book_id=instance.id)
        language_objects = [language.language for language in languages]
        res["languages"] = BookLanguageSerializer(language_objects, many=True).data

        return res
