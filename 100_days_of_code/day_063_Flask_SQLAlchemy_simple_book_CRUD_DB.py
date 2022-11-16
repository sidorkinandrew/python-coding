import os

from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object
    # to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}. {str(self.author).capitalize()} ({str(self.rating)} ⭐)>'


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # CREATE RECORD
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = Book.query.get(book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit_rating.html", book=book_selected)


if __name__ == "__main__":
    app.run(debug=True)

"""
import sqlite3

db = sqlite3.connect("books-collection.db")

cursor = db.cursor()

cursor.execute(
    "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()

"""

"""

# CRUD

# Create && commit a record
# `id` will be auto added
new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3)
db.session.add(new_book)
db.session.commit()

# Read all records
all_books = db.session.query(Book).all()

# Get one item via query
book = Book.query.filter_by(title="Harry Potter").first()

# Update a record via query
book_to_update = Book.query.filter_by(title="Harry Potter").first()
book_to_update.title = "Harry Potter and the Chamber of Secrets"
db.session.commit()

# Update a record via known primary key
book_id = 1
book_to_update = Book.query.get(book_id)
book_to_update.title = "Harry Potter and the Goblet of Fire"
db.session.commit()

# Delete a record by known primary key
book_id = 1
book_to_delete = Book.query.get(book_id)
db.session.delete(book_to_delete)
db.session.commit()
"""

####
# add.html

"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add Book</title>
</head>
<body>
    <form action="{{ url_for('add') }}" method="POST">
        <label>Book Name</label>
        <input name="title" type="text">
        <label>Book Author</label>
        <input name="author" type="text">
        <label>Rating</label>
        <input name="rating" type="text">
        <button type="submit">Add Book</button>
    </form>
</body>
</html>
"""

####
# edit_rating,html

"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Edit Rating</title>
</head>
<body>
<form action="{{ url_for('edit') }}" method="POST">
    <p>Book Name: {{book.title}}</p>
    <p>Book Author: {{book.author}}</p>
    <p>Current Rating {{book.rating}}</p>
    <input hidden="hidden" name="id" value="{{book.id}}">
    <input name="rating" type="text" placeholder="New Rating">
    <button type="submit">Change Rating</button>
</form>
</body>
</html>
"""

####
# index.html

"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Library</title>
</head>
<body>
<h1>My Library</h1>
{% if books == []: %}
<p>Library is empty.</p>
{% endif %}
<ul>
    {% for book in books %}
    <li>
        <a href="{{ url_for('delete', id=book.id) }}">Delete</a>
        {{book.title}} - {{book.author}} - {{book.rating}}/10
        <a href="{{ url_for('edit', id=book.id) }}">Edit Rating</a>
    </li>
    {% endfor %}
</ul>
<a href="{{ url_for('add') }}">Add New Book</a>
</body>
</html>
"""
