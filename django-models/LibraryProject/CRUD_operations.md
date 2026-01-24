# CRUD Operations for Book Model

## 1. Create

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>
books = Book.objects.all()
books
# Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>
book.title = "Nineteen Eighty-Four"
book.save()
book
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>
book.delete()
Book.objects.all()
# Output: <QuerySet []>

---

## **Step 4: Save and exit**

- In `vi`: Press `Esc` → type `:wq` → Enter  

---

## **Step 5: Verify file**

```bash
cat CRUD_operations.md


