from django.urls import path
from api import views

urlpatterns = [path("books/", views.BooksView.as_view())]
