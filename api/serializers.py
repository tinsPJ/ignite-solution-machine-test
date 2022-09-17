from rest_framework import serializers
from .models import (
    BooksBook,
    BooksAuthor,
    BooksLanguage,
    BooksSubject,
    BooksBookshelf,
    BooksFormat,
)


class BookAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthor
        fields = "__all__"


class BookLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksLanguage
        fields = "__all__"


class BookSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksSubject
        fields = "__all__"


class BookShelvesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksBookshelf
        fields = "__all__"


class BooksFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksFormat
        exclude = ("id", "book_id")


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksBook
        fields="__all__"

    def to_representation(self, instance):
        res = super().to_representation(instance)

        # appending author details
        authors = [author.author for author in instance.author.all()]
        res["authors"] = BookAuthorSerializer(authors, many=True).data

        # Appending language
        languages = [language.language for language in instance.language.all()]
        res["languages"] = BookLanguageSerializer(languages, many=True).data

        # Appending subject
        subjects = [subject.subject for subject in instance.subject.all()]
        res["subjects"] = BookSubjectSerializer(subjects, many=True).data

        # Appending bookshelf
        shelves = [shelf.shelf for shelf in instance.shelf.all()]
        res["shelves"] = BookShelvesSerializer(shelves, many=True).data

        # Appending
        res["formats"] = BooksFormatSerializer(instance.format.all(), many=True).data

        return res
