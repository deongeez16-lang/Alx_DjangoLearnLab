from relationship_app.models import Librarian, Library, Author, Book

# Example 1: Query all books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = Book.objects.filter(author=author)
print("Books by", author.name)
for book in books_by_author:
    print("-", book.title)

# Example 2: List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print("\nBooks in", library.name)
for book in books_in_library:
    print("-", book.title)

# Example 3: Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)
print("\nLibrarian for", library.name, "is", librarian.name)

