from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository


# Save a Book
def save(book):
    sql = "INSERT INTO books (title, author_id) VALUES (%s, %s) RETURNING *"
    values = [book.title, book.author.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book


# Select all books (show all books)
def select_all():
    books = []
    sql = "SELECT * FROM books"
    results = run_sql(sql)
    
    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row["id"])
        books.append(book)
    return books

# Delete a book
def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)