import os

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

MOVIE_DB_API_KEY = os.environ['MOVIE_DB_API_KEY']
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
Bootstrap(app)

##CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()


class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data

        response = requests.get(MOVIE_DB_SEARCH_URL, params={"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("rate_movie", id=new_movie.id))


@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)

####
# select.html

"""
{% extends 'bootstrap/base.html' %}
{% import "bootstrap/wtf.html" as wtf %}

{% block styles %}
{{ super() }}
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito+Sans:300,400,700">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,700">
<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
{% endblock %}

{% block title %}Select Movie{% endblock %}

{% block content %}
<div class="container">
    <h1 class="heading">Select Movie</h1>
    {% for movie in options: %}
    <p>
        <a href="{{ url_for('find_movie', id=movie.id) }} ">{{ movie.title }} - {{movie.release_date}}</a>
    </p>
    {% endfor %}

</div>
{% endblock %}
"""

####
# edit.html

"""
{% extends 'bootstrap/base.html' %}
{% import "bootstrap/wtf.html" as wtf %}

{% block styles %}
{{ super() }}
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito+Sans:300,400,700">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,700">
<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
{% endblock %}

{% block title %}Edit Movies{% endblock %}

{% block content %}
<div class="content">
    <h1 class="heading">{{movie.title}}</h1>
    <p class="description">Edit Movie Rating</p>
    {{ wtf.quick_form(form, novalidate=True) }}
</div>
{% endblock %}
"""

####
# index.html

"""
{% extends 'bootstrap/base.html' %}

{% block styles %}
{{ super() }}
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito+Sans:300,400,700">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,700">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,700">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css"
      integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog=="
      crossorigin="anonymous"/>
<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
{% endblock %}

{% block title %}My Top 10 Movies{% endblock %}

{% block content %}
<div class="container">
    <h1 class="heading">My Top 10 Movies</h1>
    <p class="description">These are my all time favourite movies.</p>
    {% for movie in movies %}
    <div class="card">
        <div class="front" style="background-image: url('{{movie.img_url}}');">
            <p class="large">{{ movie.ranking }}</p>
        </div>
        <div class="back">
            <div>
                <div class="title">{{movie.title}} <span class="release_date">({{movie.year}})</span></div>
                <div class="rating">
                    <label>{{movie.rating}}</label>
                    <i class="fas fa-star star"></i>
                </div>
                <p class="review">"{{movie.review}}"</p>
                <p class="overview">{{movie.description}}</p>

                <a href="{{ url_for('rate_movie', id=movie.id) }}" class="button">Update</a>
                <a href="{{ url_for('delete_movie', id=movie.id) }}" class="button delete-button">Delete</a>

            </div>
        </div>
    </div>
    {% endfor %}
</div>
<div class="container text-center add">
    <a href="{{ url_for('add_movie') }}" class="button">Add Movie</a>
</div>

{% endblock %}
"""

####
# add.html

"""
{% extends 'bootstrap/base.html' %}
{% import "bootstrap/wtf.html" as wtf %}

{% block styles %}
{{ super() }}
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito+Sans:300,400,700">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Poppins:300,400,700">
<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
{% endblock %}

{% block title %}Add Movie{% endblock %}

{% block content %}
<div class="content">
    <h1 class="heading">Add a Movie</h1>
    {{ wtf.quick_form(form, novalidate=True) }}
</div>
{% endblock %}
"""
