from flask_restful import Resource
from flask import request, make_response, jsonify
import json
#local imports
from app.api.books.v1.models import BooksModel, books_list
from app.utilities.validations import check_space,check_words,check_borrow,check_return

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
  
        new_book = db.add_book(title,author,category)
        if new_book == 'Book already exists':
            return make_response(jsonify({
            'message':'Book already exists',
            }),400)
        return make_response(jsonify({
            'message':'Book has been posted successfully',
            'book_ID': new_book['id']
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
                'book_ID': new_details
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

        if not check_borrow(status):
            return make_response(jsonify({
                'message':'Wrong status format. Use `borrow`',
            }),400)

        new_status = db.borrow_book(id)
        if new_status:
            return make_response(jsonify({
                'message':'book borrowed successfully',
                'book_ID': new_status['id'],
                'status':new_status['status']
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

        if not check_return(status):
            return make_response(jsonify({
                'message':'Wrong status format. Use `return`',
            }),400)
            
        new_status = db.return_book(id)
        if new_status:
            return make_response(jsonify({
                'message':'Book has been returned',
                'book_ID': new_status['id'],
                'status':new_status['status']
            }),200)
        else:
            return make_response(jsonify({
                'message':'Invalid ID no book found'
            }),400)

class UnreturnedBooks(Resource):
    """
        Method for retrieving all the unreturned books
    """
    def get(self):
        """
            Method for retrieving all the unreturned books
        """
        unreturned_books = db.get_unreturned()
        print(unreturned_books)
        if unreturned_books:
            return make_response(jsonify({
                'message':'Books not returned by user',
                'book': unreturned_books
            }),200)
        else:
            return make_response(jsonify({
                'message':'All books have been returned'
            }),400)