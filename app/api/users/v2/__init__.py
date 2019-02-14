from flask import Blueprint
from flask_restful import Resource,Api
#local imports
from app.api.users.v2.views import Register,Login,GetUnreturned,\
                                    GetBorrowHistory

users_v2 = Blueprint('user_v2',__name__,url_prefix='/api/v2')

api = Api(users_v2)

api.add_resource(Register,'/users/register')
api.add_resource(Login,'/users/login')
api.add_resource(GetUnreturned,'/users/books/unreturned/<int:id>')
api.add_resource(GetBorrowHistory,'/users/books/history/<int:id>')