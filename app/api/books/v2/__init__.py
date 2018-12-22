from flask import Blueprint
from flask_restful import Resource,Api
#local imports
from app.api.books.v2.views import BooksViews

library_v2 = Blueprint('lbv2',__name__,url_prefix='/api/v2')

api = Api(library_v2)

api.add_resource(BooksViews,'/books')