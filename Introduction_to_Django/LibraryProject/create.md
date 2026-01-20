# Create Book

```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
# Output: <Book: 1984 by George Orwell (1949)>

- The first code block shows the **exact Python commands** you ran in the Django shell to **create a book**.  
- The `# Output:` line shows what Django returned.

Save and exit (`Esc → :wq → Enter`).

---

## **Step 2: Edit `retrieve.md`**

```bash
vi retrieve.md
# Retrieve Book

```python
books = Book.objects.all()
books
# Output: <QuerySet [<Book: 1984 by George Orwell (1949)>]>
# Update Book

```python
book.title = "Nineteen Eighty-Four"
book.save()
book
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>

- Shows **how you updated the book’s title**.  

Save and exit.

---

## **Step 4: Edit `delete.md`**

```bash
vi delete.md
# Delete Book

```python
book.delete()
Book.objects.all()
# Output: <QuerySet []>

- Shows **how you deleted the book**.  
- The empty QuerySet confirms deletion.

Save and exit.

---

## ✅ Step 5: Verify files exist

```bash
l
