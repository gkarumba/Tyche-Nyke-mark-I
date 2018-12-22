from flask_restful import Resource
from flask import request,jsonify,make_response
#local imports
from app.api.books.v2.models import BooksModel
from app.utilities.validations import check_space,check_words
book = BooksModel()

class BooksViews(Resource):
    """
    class for the methods to add and retrieve all books
    """
    def post(self):
        """
        Method for adding a new book
        """
        try:
            data = request.get_json()
            title = data['title']
            author = data['author']
            category = data['category']
        except Exception:
            return make_response(jsonify({
                'message':'Invalid key field'
            }),400)

        if not check_space(title) or not check_words(title):
            return make_response(jsonify({
            'message':'Title field cannot be empty',
            }),400)

        if not check_words(author):
            return make_response(jsonify({
            'message':'Author takes only letters',
            }),400)

        if not check_words(category):
            return make_response(jsonify({
            'message':'category takes only letters',
            }),400)

        response = book.check_book(title)
        if not response:
            books = book.add_book(title,author,category)
            # print(books)
            if books:
                return make_response(jsonify({
                    'message':'Book added successfully',
                    'book_id':books['id']
                }),200)
        else: 
            return make_response(jsonify({
                'message':'Book already exists',
            }),400)
