from flask_restful import Resource
from flask import request,jsonify,make_response
#local imports
from app.api.books.v2.models import BooksModel
from app.utilities.validations import check_space,check_words,\
                                      check_borrow
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

class EditTitle(Resource):
    """
    Class for the methods to edit a book's title
    """
    def put(self,id):
        """
        Method to edit a book title
        """
        try:
            data = request.get_json()
            title = data['new_title']
        except Exception:
            return make_response(jsonify({
                'message':'Invalid key field'
            }),400)

        if not check_space(title) or not check_words(title):
            return make_response(jsonify({
            'message':'new_title field cannot be empty',
            }),400)  
    
        response = book.edit_book_title(title,id)
        if response:
            return make_response(jsonify({
                'message':'Book edited successfully',
                'book_id':response
            }),200)
        else: 
            return make_response(jsonify({
                'message':'Invalid ID.No book found'
            }),400)

class EditAuthor(Resource):
    """
    Class for the methods to edit a book's author
    """
    def put(self,id):
        """
        Method to edit a book's author
        """
        try:
            data = request.get_json()
            author = data['new_author']
        except Exception:
            return make_response(jsonify({
                'message':'Invalid key field'
            }),400)

        if not check_space(author) or not check_words(author):
            return make_response(jsonify({
            'message':'new_author field cannot be empty',
            }),400)  
    
        response = book.edit_book_author(author,id)
        if response:
            return make_response(jsonify({
                'message':'Book edited successfully',
                'book_id':response
            }),200)
        else: 
            return make_response(jsonify({
                'message':'Invalid ID.No book found'
            }),400)

class EditCategory(Resource):
    """
    Class for the methods to edit a book's category
    """
    def put(self,id):
        """
        Method to edit a book's category
        """
        try:
            data = request.get_json()
            category = data['new_category']
        except Exception:
            return make_response(jsonify({
                'message':'Invalid key field'
            }),400)

        if not check_space(category) or not check_words(category):
            return make_response(jsonify({
            'message':'new_category field cannot be empty',
            }),400)  
    
        response = book.edit_book_category(category,id)
        if response:
            return make_response(jsonify({
                'message':'Book edited successfully',
                'book_id':response
            }),200)
        else: 
            return make_response(jsonify({
                'message':'Invalid ID.No book found'
            }),400)

class BorrowBook(Resource):
    """
    Class with the method to borrow a book
    """
    def post(self,id):
        """
        Method for borrowing a book
        """
        try:
            data = request.get_json()
            status = data['status']
        except Exception:
            return make_response(jsonify({
                'message':'Invalid key field'
            }),400)
        if not check_borrow(status):
            return make_response(jsonify({
                'message':'Title field cannot be empty',
            }),400)
        check_status = book.check_status(id)
        if not check_status:
            return make_response(jsonify({
                'message':'Book is Unavailable'
            }),400)
        response = book.borrow_book(status,id)
        if response:
            return make_response(jsonify({
                'message':'Book borrowed successfully',
                'book_id':response
            }),201)
        else: 
            return make_response(jsonify({
                'message':'Invalid ID.No book found'
            }),400)

