# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BooksAuthor(models.Model):
    id = models.IntegerField(primary_key=True)
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = "books_author"


class BooksBook(models.Model):
    id = models.IntegerField(primary_key=True)
    download_count = models.IntegerField(blank=True, null=True)
    gutenberg_id = models.IntegerField()
    media_type = models.CharField(max_length=16)
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "books_book"
        ordering = ["-download_count"]


class BooksBookAuthors(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey(
        BooksBook, db_column="book_id", on_delete=models.PROTECT, related_name="author"
    )
    author_id = models.IntegerField()

    @property
    def author(self):
        return BooksAuthor.objects.get(pk=self.author_id) if self.author_id else None

    class Meta:
        managed = False
        db_table = "books_book_authors"


class BooksBookBookshelves(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey(
        BooksBook, db_column="book_id", on_delete=models.PROTECT, related_name="shelf"
    )
    bookshelf_id = models.IntegerField()

    @property
    def shelf(self):
        return (
            BooksBookshelf.objects.get(pk=self.bookshelf_id)
            if self.bookshelf_id
            else None
        )

    class Meta:
        managed = False
        db_table = "books_book_bookshelves"


class BooksBookLanguages(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey(
        BooksBook,
        db_column="book_id",
        on_delete=models.PROTECT,
        related_name="language",
    )
    language_id = models.IntegerField()

    @property
    def language(self):
        return (
            BooksLanguage.objects.get(pk=self.language_id) if self.language_id else None
        )

    class Meta:
        managed = False
        db_table = "books_book_languages"


class BooksBookSubjects(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.ForeignKey(
        BooksBook, db_column="book_id", on_delete=models.PROTECT, related_name="subject"
    )
    subject_id = models.IntegerField()

    @property
    def subject(self):
        return BooksSubject.objects.get(pk=self.subject_id) if self.subject_id else None

    class Meta:
        managed = False
        db_table = "books_book_subjects"


class BooksBookshelf(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = "books_bookshelf"


class BooksFormat(models.Model):
    id = models.IntegerField(primary_key=True)
    mime_type = models.CharField(max_length=32)
    url = models.TextField()
    book_id = models.ForeignKey(
        BooksBook, db_column="book_id", on_delete=models.PROTECT, related_name="format"
    )

    class Meta:
        managed = False
        db_table = "books_format"


class BooksLanguage(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = "books_language"


class BooksSubject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = "books_subject"
