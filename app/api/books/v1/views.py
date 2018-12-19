from flask_restful import Resource
from flask import request, make_response, jsonify
import json
#local imports
from app.api.books.v1.models import BooksModel, books_list

db = BooksModel()

class AddBook(Resource):
    """
        Class for adding a book
    """
    def post(self):
        """
            Method for posting a book
        """
        data = request.get_json()
        title = data['title']
        author = data['author']
        category = data['category']
  
        new_book = db.add_book(title,author,category)
        if new_book == 'Book already exists':
            return make_response(jsonify({
            'message':'Book already exists',
            }),400)
        return make_response(jsonify({
            'message':'Book has been posted successfully',
            'book': new_book
        }),201)
        
                
       

