from django.shortcuts import render

# Create your views here.
from .Librarian_Crud.librarian_registertation import LibrarianRegistrationApi
from .Librarian_Crud.library_login import LibraryLoginApi
from .Librarian_Crud.add_books_post import BokksPostApi
from .Librarian_Crud.books_update_api import BooksUpdateApi
from .Librarian_Crud.delete_book_api import DeleteBookApi
from .Librarian_Crud.member_post_api import MembersRegistrationApi
from .Librarian_Crud.update_member_api import MemberUpdateApi
from .Librarian_Crud.get_member_api import MembersGetApi
from .Librarian_Crud.delete_member import DeleteMember

LibrarianRegistrationApi()
LibraryLoginApi()
BokksPostApi()
BooksUpdateApi()
DeleteBookApi()
MembersRegistrationApi()
MemberUpdateApi()
MembersGetApi()
DeleteMember()