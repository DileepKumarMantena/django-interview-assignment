from django.shortcuts import render

# Create your views here.
from .Librarian_Crud.librarian_registertation import LibrarianRegistrationApi
from .Librarian_Crud.library_login import LibraryLoginApi

LibrarianRegistrationApi()
LibraryLoginApi()