from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return []

# List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return Librarian.objects.get(library=library)
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# Example usage (can be commented out in production)
if __name__ == "__main__":
    # Print books by author "John Doe"
    books = books_by_author("John Doe")
    print("Books by John Doe:", [book.title for book in books])

    # Print books in library "Central Library"
    library_books = books_in_library("Central Library")
    print("Books in Central Library:", [book.title for book in library_books])

    # Print librarian of "Central Library"
    librarian = librarian_for_library("Central Library")
    if librarian:
        print("Librarian of Central Library:", librarian.name)
    else:
        print("No librarian found for Central Library")

