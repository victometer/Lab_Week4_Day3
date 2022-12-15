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

def select(id):
    book = None
    sql = 'SELECT * FROM books WHERE id = %s'
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], author, result['id'])
    return book


# Delete a book
def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# add a book
# show a book
# why the above 2 aren't here, but in the controller?
# How does the if statement work in the select(id)?