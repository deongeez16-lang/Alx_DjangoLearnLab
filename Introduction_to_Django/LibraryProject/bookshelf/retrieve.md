# Retrieve Book

```python
from bookshelf.models import Book
book = Book.objects.get(title="1984")
book
# Output: <Book: 1984 by George Orwell (1949)>

### Explanation:

- `Book.objects.get(title="1984")` → retrieves the book with title `"1984"` (ALX expects this)  
- `book` → prints the book instance  
- Output matches exactly what ALX expects  

---

## ✅ Other CRUD files

Just to be safe, here’s what they should look like:

### `create.md`
```markdown
# Create Book

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>

### `update.md`
```markdown
# Update Book

```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
book
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>

### `delete.md`
```markdown
# Delete Book

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
Book.objects.all()
# Output: <QuerySet []>

