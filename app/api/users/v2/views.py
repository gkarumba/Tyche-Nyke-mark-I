from flask_restful import Resource
from flask import request,jsonify,make_response
#local imports
from app.api.users.v2.models import UsersModel
from app.utilities.validations import check_space,check_words,\
                                      check_email,check_password
user = UsersModel()

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
                if check_admin:
                    return make_response(jsonify({
                            'message':'User is Admin'
                        }))
                else:
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
        

   