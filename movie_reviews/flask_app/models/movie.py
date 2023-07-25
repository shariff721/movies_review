from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user, review
from flask import flash


class Movie:
    db = "movies"

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']

    @classmethod
    def save_movie(cls, data):
        query = " INSERT INTO movies (title) VALUES (%(title)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all_movies(cls):
        query = """
            SELECT * FROM movies;
        """
        results = connectToMySQL(cls.db).query_db(query)
        all_movies = []
        for one_movie in results:
            all_movies.append(cls(one_movie))
        return all_movies

    @classmethod
    def get_one_movie(cls, data):
        query = """
            SELECT * FROM movies
            WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update_movie(cls, data):
        query = """
            UPDATE movies
            SET title = %(title)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete_movie(cls, data):
        query = """
            DELETE FROM movies WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_movie(movie):
        is_valid = True

        if len(movie['title']) < 3:
            flash("movie title must not be blank.")
            is_valid = False

        return is_valid
