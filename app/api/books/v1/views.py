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
        
    def get(self):
        """
            Method for getting all books
        """
        all_books = db.get_all()
        return make_response(jsonify({
            'message':'OK',
            'book': all_books
        }),200)
       
class GetBook(Resource):
    """
        Class for method of getting one book
    """ 
    def get(self,id):
        """
            Method for retrieving one book
        """
        one_book = db.get_one(id)
        if one_book:
            return make_response(jsonify({
                'message':'OK',
                'book': one_book
            }),200)
        else:
            return make_response(jsonify({
                'message':'Invalid ID no book found'
            }),400)

class EditBook(Resource):
    """
        Class for method of editing a book's details
    """
    def put(self,id):
        """
            Method for editing a book's details
        """
        data = request.get_json()
        title = data['updated_title']
        author = data['updated_author']
        category = data['updated_category']

        new_details = db.edit_book(id,title,author,category)
        if new_details:
            return make_response(jsonify({
                'message':'book edited successfully',
                'book': new_details
            }),200)
        else:
            return make_response(jsonify({
                'message':'Invalid ID no book found'
            }),400)

class BorrowBook(Resource):
    """
        Class for method of borrowing book
    """
    def put(self,id):
        """
            Method for allowing users to borrow a book
        """
        data = request.get_json()
        status = data['updated_status']

        new_status = db.borrow_book(id,status)
        if new_status:
            return make_response(jsonify({
                'message':'book borrowed successfully',
                'book': new_status
            }),200)
        else:
            return make_response(jsonify({
                'message':'Invalid ID no book found'
            }),400)

class ReturnBook(Resource):
    """
        Class for method of returning borrowed books
    """
    def put(self,id):
        """
            Method for allowing users to return a borrowed book
        """
        data = request.get_json()
        status = data['updated_status']

        new_status = db.borrow_book(id,status)
        if new_status:
            return make_response(jsonify({
                'message':'Book has been returned',
                'book': new_status
            }),200)
        else:
            return make_response(jsonify({
                'message':'Invalid ID no book found'
            }),400)