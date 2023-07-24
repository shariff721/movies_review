from flask import render_template, redirect, session, request
from flask_app import app

from flask_app.models import user, review



# Visible routes
@app.route("/dashboard")
def home_page():
    return render_template("dashboard.html")

@app.route("/comments")
def all_posted_reviews_page():
    if 'user_id' not in session:
        return redirect('/')
    data ={
        'id': session['user_id']
    }
    return render_template("posted_reviews.html", user_logged = user.User.get_user_by_id(data))

@app.route("/new/review")
def add_review_page():
    if 'user_id' not in session:
        return redirect("/")
    data ={
        'id': session['user_id']
    }
    return render_template("new_review.html", user_logged = user.User.get_user_by_id(data))

@app.route("/edit/<int:id>")
def edit_review_page(id):
    pass


@app.route("/show/<int:id>")
def review_info_page(id):
    if 'user_id' not in session:
        return redirect('/')
    data ={
        'id': id,
    }
    form_data = {
        'id': session['user_id']
    }
    print(request.form)
    return render_template("show_review.html", user_logged = user.User.get_user_by_id(form_data), {{  }})


# Hidden routes
@app.route("/reviews/<int:id>/delete")
def delete(id):
    pass

@app.route("/reviews/add_to_db", methods=["POST"])
def add_review_to_db():
    pass

@app.route("/reviews/<int:id>/edit_in_db", methods=["POST"])
def update(id):
    pass
