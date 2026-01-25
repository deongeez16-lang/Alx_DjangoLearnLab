from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

import renderst_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view: library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

ews.py
cd /Alx_DjangoLearnLab/django-models/LibraryProject/relationship_app
vi views.py














 

