from flask import Blueprint
from flask_restful import Resource,Api
#local imports
from app.api.books.v2.views import AddBooks,GetBook,EditTitle,EditAuthor,\
                                   EditCategory,BorrowBook,ReturnBook

library_v2 = Blueprint('lbv2',__name__,url_prefix='/api/v2')

api = Api(library_v2)

api.add_resource(AddBooks,'/books')
api.add_resource(GetBook,'/books/<int:id>')
api.add_resource(EditTitle,'/books/title/<int:id>')
api.add_resource(EditAuthor,'/books/author/<int:id>')
api.add_resource(EditCategory,'/books/category/<int:id>')
api.add_resource(BorrowBook,'/books/borrow/<int:id>')
api.add_resource(ReturnBook,'/books/return/<int:id>')