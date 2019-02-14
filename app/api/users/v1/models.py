from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
users_list = []
"""
    List for storing the users added
"""

class UsersModel:
    """
        Class for the users endpoints
    """
    user_id = 1
    def __init__(self,email,username,password):
        """
            Constructor method for the class UsersModel
        """
        self.id = UsersModel.user_id
        self.password = generate_password_hash(password)
        self.username = username
        self.email = email

        UsersModel.user_id += 1

    def add_user(self,email,username,password):
        """
            Method for serializing the data of a user
        """
        payload = {
            'email' : email,
            'username' : username,
            'password' : generate_password_hash(password),
            'id' : len(users_list)+1,
            'added_on'  : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        } 
        check_email = self.validate_email(email)
        # print(check_email)
        if check_email:
            return False
        else:
            users_list.append(payload)
            for pos in users_list:
                return pos
            
    def validate_email(self,email):
        """
            Method for checking if a user is already registered
        """
        for user in users_list:
            if user.email == email:
                return True
            else:
                return False
    
    def validate_user_login(self,email,password):
        """
        Method for checking the password
        """
        for user in users_list:
            # if email == user['email']:
            #     # print(user['email'])
            password_check = user.password
            print(password_check)
            validate_password = check_password_hash(password_check,password)
            print(validate_password)
            if validate_password:
                for pos in users_list:
                    return pos
            return False
            # else:
            #     return False

    
    def validate_password(self,password):
        """
        Method to validate password
        """
        for user in users_list:
            if check_password_hash(user.password,password):
                return True
            return False

    def serialize(self):
        """
        Method to take json data and return a python dictionary
        """
        return {
            "id":self.id,
            "username":self.username,
            "email":self.email,
            "password":self.password
        }
      
