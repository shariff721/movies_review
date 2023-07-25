from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user, review, movie
from flask import flash

class Review:
    db = "movies"

    def __init__(self, data):
        self.id = data['id']
        self.body = data['body']
        self.recommended = data['recommended']
        self.date_reviewed = data['date_reviewed']
        self.user_id = data['user_id']
        self.movie_id = data['movie_id']
        
        
    @classmethod
    def save_review(cls, data):
        query = "INSERT INTO reviews (body,recommended,date_reviewed,user_id,movie_id) VALUES(%(body)s,%(recommended)s,%(date_reviewed)s,%(user_id)s,%(movie_id)s)"
        return connectToMySQL(cls.db).query_db(query, data)
    
    
    @classmethod
    def review_update(cls,data):
        query = """
            UPDATE reviews
            SET body = %(body)s, recommended = %(recommended)s, date_reviewed = %(date_reviewed)s
            WHERE id = %(id)s;
        """
        return connectToMySQL(cls.db).query_db(query, data)
    
    def get_movie_name(self):
        query = " SELECT title FROM movies WHERE id = %(movie_id)s;"
        data = {"movie_id": self.movie_id}
        result = connectToMySQL(self.db).query_db(query, data)
        return result[0]['title']
    
    def get_first_name(self):
        query = " SELECT first_name FROM users WHERE id = %(user_id)s;"
        data = {"user_id": self.user_id}
        result = connectToMySQL(self.db).query_db(query, data)
        return result[0]['first_name']
    
    @classmethod
    def get_all_reviews(cls):
        query = "SELECT * FROM reviews;"
        results = connectToMySQL(cls.db).query_db(query)

        all_reviews = []
        for one_review in results:
            all_reviews.append(cls(one_review))
        return all_reviews
    
    
    @classmethod
    def delete_review(cls, data):
        query = """
                DELETE FROM reviews WHERE id = %(id)s;
            """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_one_review(cls, data):
        query = """
            SELECT * FROM reviews WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])