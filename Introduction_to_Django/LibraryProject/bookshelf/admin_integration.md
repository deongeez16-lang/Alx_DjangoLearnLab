# Django Admin Integration for Book Model

The Book model was registered with the Django admin interface in `bookshelf/admin.py`.

## Admin Customization
The admin interface was customized using a `BookAdmin` class with the following configurations:

- Displayed fields: title, author, publication_year
- Search fields: title, author
- List filter: publication_year

## Admin Access
A superuser was created using:

python3 manage.py createsuperuser

The Django admin interface was accessed at:

http://127.0.0.1:8000/admin/

This allows full management of Book records through the admin panel.

