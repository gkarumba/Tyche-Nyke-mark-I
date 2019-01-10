from flask_restful import Resource
from flask import request,jsonify,make_response
#local imports
from app.api.books.v2.models import BooksModel
from app.utilities.validations import check_space,check_words
book = BooksModel()

class AddBooks(Resource):
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
                }),201)
        else: 
            return make_response(jsonify({
                'message':'Book already exists',
            }),400)

    def get(self):
        """
        Method to retrieve all the books
        """
        response = book.get_all_books()
        if response:
            return make_response(jsonify({
                    'message':'Books in the library',
                    'books':response
                }),200)
        else:
            return make_response(jsonify({
                'message':'No books in the library'
            }),400)
            
class GetBook(Resource):
    """
    Class for the method to get one book
    """
    def get(self,id):
        """
        Method to get one book
        """
        response = book.get_one_book(id)
        if response:
            return make_response(jsonify({
                'message':'Book Found',
                'books':response
            }),200)
        else:
            return make_response(jsonify({
                'message':'Invalid ID.No book found'
            }),400)