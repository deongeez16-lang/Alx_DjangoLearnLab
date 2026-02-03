from django.urls import path
# from .views import list_books, LibraryDetailView
from . import views
# from .views import UserLoginView, UserLogoutView, register
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # function-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    # path('login/', UserLoginView.as_view(), name='login'),
    # path('logout/', UserLogoutView.as_view(), name='logout'),
    # path('register/', register, name='register'),
       path(
        'login/',
        LoginView.as_view(template_name='relationship_app/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(template_name='relationship_app/logout.html'),
        name='logout'
    ),
    path(
        'register/',
        views.register,
        name='register'
    ),
]

