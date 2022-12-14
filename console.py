import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author1 = Author("J.K Rowling")
author_repository.save(author1)

book1 = Book("Harry Potter 1", author1)
book_repository.save(book1)
book2 = Book("Harry Potter 2", author1)
book_repository.save(book2)