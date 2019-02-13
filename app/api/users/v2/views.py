from flask_restful import Resource
from flask import request,jsonify,make_response
import json
#local imports
from app.utilities.token import TokenClass
from app.api.users.v2.models import UsersModel
from app.utilities.validations import check_space,check_words,\
                                      check_email,check_password

user = UsersModel()
tk = TokenClass()

class Register(Resource):
    """
    class for the methods to add users
    """
    def post(self):
        """
        Method for adding a new user
        """
        try:
            data = request.get_json()
            email = data['email']
            password = data['password']
            username = data['username']
        except Exception:
            return make_response(jsonify({
                'message':'Invalid key field'
            }),400)

        if not check_space(username) or not check_words(username):
            return make_response(jsonify({
            'message':'username field cannot be empty',
            }),400)

        if not check_email(email):
            return make_response(jsonify({
            'message':'Wrong Email format',
            }),400)

        if not check_password(password):
            return make_response(jsonify({
            'message':'Password takes a minimum of 8 characters',
            }),400)

        response = user.check_email(email)
        if not response:
            users = user.add_user(email,password,username)
            # print(users)
            if users:
                check_admin = user.set_role(users['id'])
                if not check_admin:
                #     return make_response(jsonify({
                #             'message':'User is Admin'
                #         }))
                # else:
                    return make_response(jsonify({
                                'message':'User not Admin'
                            }))
                return make_response(jsonify({
                    'message':'User has been added successfully',
                    'user_id':users['id']
                }),201)
        else: 
            return make_response(jsonify({
                'message':'user already exists',
            }),400)
        
class Login(Resource):
    """
    Class with the Method to allow user to login
    """
    def post(self):
        """
        Method to allow the user to login
        """
        try:
            data = request.get_json()
            email = data['email']
            password = data['password']
        except Exception:
            return make_response(jsonify({
                'message':'Invalid input field'
            }),200)
        
        if not check_email(email):
            return make_response(jsonify({
                'message':'Wrong Email format',
            }),400)
        # print(check_password(password))
        if not check_password(password):
            return make_response(jsonify({
                'message':'Password takes a minimum of 8 characters',
            }),400)

        validate_email = user.check_email(email)
        if not validate_email:
            return make_response(jsonify({
                'message':'Invalid Email Address'
            }),400)

        validate_password = user.validate_password(email,password)
        # print(validate_email)
        # print(validate_password)
        if not validate_password:
            return make_response(jsonify({
                'message':'Invalid logging credentials'
            }),400)
        
        user_id = validate_email['id']
        user_token = tk.encode_token(user_id)
        # print(user_token)

        if not user_token:
            return make_response(jsonify({
                'message':'Token Generation Unsuccessful'
            }),401)
        return make_response(jsonify({
                'message':'User logged in successfully',
                'user_id': user_id,
                'token': user_token
            }),200)

class GetUnreturned(Resource):
    """
    Class with method to get books not returned by user
    """
    def get(self,id):
        """
        Method to get Unreturned books by a user
        """
        from app.utilities.token import TokenClass as tk
        validate_token = tk.validate_authentication(self)
        if not validate_token:
            return make_response(jsonify({
                'message':'Token Validation Failed'
            }),400)
        response = tk.decode_token(self,validate_token)
        if isinstance(response,str):
            return make_response(jsonify({
                'message':'Invalid Token.Please Login'
            }),400)

        check_role = user.check_role(response)
        # print(check_role)
        if not check_role:
            return make_response(jsonify({
                'message':'Only Admin is allowed to check for unreturned books'
            }),401)

        get_books = user.get_unreturned_books(id)
        if not get_books:
            return make_response(jsonify({
                'message':'User has no borrowed books'
            }),400)
        return make_response(jsonify({
                'message':'Books not returned by user',
                'books': get_books
            }),200)

class GetBorrowHistory(Resource):
    """
    Class with method to get a user's borrowing history
    """
    def get(self,id):
        """
        Method to get a user's borrowing history
        """
        from app.utilities.token import TokenClass as tk
        validate_token = tk.validate_authentication(self)
        if not validate_token:
            return make_response(jsonify({
                'message':'Token Validation Failed'
            }),400)
        response = tk.decode_token(self,validate_token)
        if isinstance(response,str):
            return make_response(jsonify({
                'message':'Invalid Token.Please Login'
            }),400)

        get_books = user.get_borrowing_history(id)
        if not get_books:
            return make_response(jsonify({
                'message':'Invalid User ID'
            }),400)
        return make_response(jsonify({
                'message':'Books borrowed by user',
                'books': get_books
            }),200)
