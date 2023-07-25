from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models import user, review, movie


@app.route("/dashboard")
def home_page():
    all_movies = movie.Movie.get_all_movies()
    return render_template("dashboard.html", all_movies=all_movies)
