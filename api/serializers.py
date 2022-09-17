from rest_framework import serializers
from .models import (BooksBook, BooksBookAuthors, BooksAuthor,
                     BooksBookLanguages, BooksLanguage, BooksSubject,
                     BooksBookSubjects, BooksBookBookshelves, BooksBookshelf,
                     BooksFormat)
from typing import ClassVar


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
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = BooksBook
        fields = ("title", "media_type", "download_count")

    def get_related_instance(self, model: object, instance: object) -> object:
        return model.objects.filter(book_id=instance.id)

    def to_representation(self, instance):
        res = super().to_representation(instance)
        # appending author details
        authors = self.get_related_instance(BooksBookAuthors, instance)
        author_objects = [author.author for author in authors]
        res["authors"] = BookAuthorSerializer(author_objects, many=True).data

        # Appending language
        languages = self.get_related_instance(BooksBookLanguages, instance)
        language_objects = [language.language for language in languages]
        res["languages"] = BookLanguageSerializer(language_objects,
                                                  many=True).data

        # Appending subject
        subjects = self.get_related_instance(BooksBookSubjects, instance)
        subject_object = [subject.subject for subject in subjects]
        res['subjects'] = BookSubjectSerializer(subject_object, many=True).data

        # Appending bookshelf
        shelfs = self.get_related_instance(BooksBookBookshelves, instance)
        shelf_objects = [shelf.shelf for shelf in shelfs]
        res['shelves'] = BookShelvesSerializer(shelf_objects, many=True).data

        # Appending 

        return res
