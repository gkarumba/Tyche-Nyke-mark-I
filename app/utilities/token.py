import os
import datetime
import jwt
import json
from werkzeug.exceptions import Unauthorized,BadRequest,NotFound
from flask import request,make_response,jsonify
from functools import wraps
#local imports
key = os.getenv('SECRET_KEY')
from app.api.users.v2.models import UsersModel

db = UsersModel()

class Token():
    """
    Class with methods to encode and decode tokens
    """
    def encode_token(self,user_id):
        """
        Method to Generate token
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=10),
                'iat': datetime.datetime.utcnow(),
                'id': user_id
            }
            token = jwt.encode(payload,key,algorithm='HS256')
            valid_token = token.decode('utf-8')
            return valid_token
            
        except Exception as error:
            return str(error)

    def decode_token(self,auth_token):
        """
        Method to decode Token
        """
        try:
            payload = jwt.decode(auth_token,key)
        except jwt.ExpiredSignatureError:
            raise Unauthorized('Session has expired')
        except jwt.InvalidTokenError:
            raise Unauthorized('Invalid Token,Please log in')

        return payload['id']

# class ValidateAuthentication(Token):
def validate_authentication(auth):
    """
    Method to validate the authentication for protected routes
    """
    @wraps(auth)
    def decorator(*args,**kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[0]
        else:
            auth_token = ''
        if auth_token:
            response = Token.decode_token(auth_token)
            if not isinstance(response,str):
                raise Unauthorized('Invalid Token.Please Login')
            user_creds = db.get_user_id(response)
            if not user_creds:
                raise Unauthorized('Please Log In')
            return auth(*args,**kwargs)
        return decorator
            

