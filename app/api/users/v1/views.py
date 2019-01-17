from flask_restful import Resource
from flask import request, make_response, jsonify
import json
from werkzeug.security import check_password_hash
#local imports
from app.api.users.v1.models import UsersModel,users_list
from app.utilities.validations import check_space,check_words,\
                                      check_email,check_password

class Register(Resource):
    """
        Class for adding a user
    """
    def post(self):
        """
            Method for registering a user
        """
        try:
            data = request.get_json()
            email = data['email']
            password = data['password']
            username = data['username']
        except Exception:
            return make_response(jsonify({
                'message':'Invalid input field',
            }),400)

        if not check_password(password):
            return make_response(jsonify({
            'message':'Password must be atleast 8 characters',
            }),400)

        if not check_space(username) or not check_words(username):
            return make_response(jsonify({
            'message':'Username takes only letters',
            }),400)

        if not check_email(email):
            return make_response(jsonify({
            'message':'wrong email format',
            }),400)

        new_user = UsersModel(email,password,username)
        
        for user in users_list:
            if user.email == email:
                return make_response(jsonify({
                    'message':'user already exists'
                }),400)
            else: 
                break
        users_list.append(new_user)
        return  make_response(jsonify({
            'message':'user has been registered successfully',
            'new_user': new_user.serialize()
        }),201)
        # new_user = db.add_user(email,username,password)
        # print(new_user)
        # if not new_user:
        #     return make_response(jsonify({
        #         'message':'user already exists'
        #     }),400)
        # return make_response(jsonify({
        #     'message':'user has been registered successfully',
        #     'user_ID': new_user['id']
        # }),201)

class Login(Resource):
    """
        Class for logging a user
    """
    def post(self):
        """
            Method for logging a user
        """
        try:
            data = request.get_json()
            email = data['email']
            password = data['password']
        except Exception:
            return make_response(jsonify({
                'message':'Invalid input field',
            }),400)

        if not check_password(password):
            return make_response(jsonify({
            'message':'Password must be atleast 8 characters',
            }),400)

        if not check_email(email):
            return make_response(jsonify({
            'message':'wrong email format',
            }),400)
  
        for user in users_list:
            if user.email == email:

                #  for user in users_list:
                print(user.password)
                print(check_password_hash(user.password,password))
                if check_password_hash(user.password,password):
                    return make_response(jsonify({
                        'message':'user has been logged in successfully'
                        # 'user_ID': new_user['id']
                        }),201)
               
        return make_response(jsonify({
            'message':'Wrong login details, please try again'
        }),400)