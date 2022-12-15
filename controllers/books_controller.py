from flask import render_template, Blueprint, Flask, request, redirect
from repositories import book_repository
from models.book import Book
from models.author import Author
import repositories.book_repository as book_repository
import repositories.author_repository as author_repository


books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books=books)

@books_blueprint.route("/books/<id>/delete", methods = ['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')


# does this GET method ask for the new book form? And why does it only need the author?(it doesn't - that was for the tasks that only have one user) Does save here work better than select all for adding new authors? I have no authors to select, right? i need to create and save
# @books_blueprint.route('/books/new', methods = ['GET'])
# def new_book():
#     authors = author_repository.save()
#     return render_template('books/new.html', authors = authors)

# # and does this POST method allow for the details of the new book to be entered in the form requested above?
# # How do I request a form with a box for the author's name and a book title, that haven't been put in yet?
# @books_blueprint.route('/books', methods = ['POST'])
# def create_book():
#     title = request.form['title']
#     name = request.form['author.name']
#     book = Book(title, author)
#     book_repository.save(book)
#     author = Author(name)
#     author_repository.save(author)
#     return redirect ('/books')

@books_blueprint.route('/books/<id>', methods = ['GET'])
def show_book(id):
    book = book_repository.select(id)
    return render_template('/books/show.html', book=book)

