from flask import render_template, Blueprint, Flask, request, redirect
from repositories import book_repository
from models.book import Book
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