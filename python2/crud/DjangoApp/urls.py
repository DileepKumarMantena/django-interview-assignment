from django.urls import path
from .views import *

urlpatterns = [
    path('LibrarianRegistrationApi/', LibrarianRegistrationApi.as_view(), name="To register the Librarian"),
    path('LibraryLoginApi/', LibraryLoginApi.as_view(), name="To login the Librarian"),

]
