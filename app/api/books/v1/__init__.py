from flask import Blueprint
from flask_restful import Resource,Api
#local imports
from app.api.books.v1.views import AddBook,GetBook,EditBook

library_v1 = Blueprint('book_v1',__name__,url_prefix='/api/v1')

api = Api(library_v1)

api.add_resource(AddBook,'/books')
api.add_resource(GetBook,'/books/<int:id>')
api.add_resource(EditBook,'/books/edit/<int:id>')