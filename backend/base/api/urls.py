from django.urls import path
from .views import (
    AuthorDetailView,
    BookListView,
    MyTokenObtainPairView,
    LoginView,
    RegisterView,
    ProfileView,
    ProfileUpdateView,
    AdminLoginView,
    UserListingView,
    UserDeleteView,
    UserDeatailView,
    UserUpdateView,
    AuthorCreateView,
    AuthorDeleteView,
    AuthorUpdateView,
    AuthorsListView,
    BookCreateView,
    BookDeleteView,
    BookUpdateView,
    BookDetailView,
)
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path("token/", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="Register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/update", ProfileUpdateView.as_view(), name="profile_update"),
    # Admin urls
    path("admin/login/", AdminLoginView.as_view(), name="Admin_login"),
    path("admin/users", UserListingView.as_view(), name="User_lisiting"),
    path("admin/user/delete/<pk>", UserDeleteView.as_view(), name="user_delete"),
    path("admin/user/detail/<pk>", UserDeatailView.as_view(), name="user_detail"),
    path("admin/user/update/<pk>", UserUpdateView.as_view(), name="user_update"),
    # Books
    path("books/", BookListView.as_view(), name="Book_lisiting"),
    path("books/<id>", BookDetailView.as_view(), name="Book_detail"),
    path("books/create/", BookCreateView.as_view(), name="Book_create"),
    path("books/update/<id>", BookUpdateView.as_view(), name="Book_update"),
    path("books/delete/<id>", BookDeleteView.as_view(), name="Book_delete"),
    # Authors
    path("authors/", AuthorsListView.as_view(), name="authors_lisiting"),
    path("authors/create/", AuthorCreateView.as_view(), name="author_create"),
    path("authors/update/<id>", AuthorUpdateView.as_view(), name="author_update"),
    path("authors/delete/<id>", AuthorDeleteView.as_view(), name="author_delete"),
    path("authors/<id>", AuthorDetailView.as_view(), name="author_detail"),
]
