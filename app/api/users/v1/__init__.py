from flask import Blueprint
from flask_restful import Resource,Api
#local imports
from app.api.users.v1.views import Register,Login

users_v1 = Blueprint('user_v1',__name__,url_prefix='/api/v1')

api = Api(users_v1)

api.add_resource(Register,'/users/register')
api.add_resource(Login,'/users/login')