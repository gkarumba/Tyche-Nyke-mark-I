import unittest
#local import
from app import create_app
import json

class BaseTest(unittest.TestCase):
    """
        Class for setting up the tests
    """ 
    def setUp(self):
        """
            Method for setting up the tests
        """
        self.app_test = create_app()
        self.client = self.app_test.test_client()
        self.app_test.testing = True

        self.post_data = {
            "title":"Buddies of Rome",
            "author":"Cannius Longinus",
            "category":"history"
        }
        self.edit_data = {
            "updated_title":"Allies of Rome",
            "updated_author":"Cassius Aurelius",
            "updated_category":"fiction"
        }
        self.borrow_data = {
            "updated_status":"borrow"
        }
        self.return_data = {
            "updated_status":"return"
        }
        self.unreturned_data = {
            "status":"Borrowed"
        }
        self.space_data = {
            "title":" ",
            "author":"Cannius Longinus",
            "category":"history"
        }
        self.word_data = {
            "title":"Off the pitch",
            "author":"123456",
            "category":"history"
        }
        self.borrowing_data = {
            "updated_status":"borrowing"
        }
        self.returning_data = {
            "updated_status":"returning"
        }
        self.email_data = {
            "email" : "emailgmail.com",
            "username" : "johnny",
            "password" : "barca12345"
        }
        self.invalid_email_data = {
            "" : "emailgmail.com",
            "username" : "johnny",
            "password" : "barca12345"
        }
        self.password_data = {
            "email" : "email@gmail.com",
            "username" : "johnny",
            "password" : "12t"
        }
        self.invalid_password_data = {
            "email" : "email@gmail.com",
            "username" : "johnny",
            "" : "12t"
        }
        self.invalid_username_data = {
            "email" : "email@gmail.com",
            "" : "johnny",
            "password" : "12t"
        }
        self.register_data = {
            "email" : "john@gmail.com",
            "username" : "johnny",
            "password" : "126735ttwywibe"
        }
        self.login_user = {
            "email" : "john@gmail.com",
            "password" : "126735ttwywibe"
        }
        self.login_wrong_password = {
            "email" : "john@gmail.com",
            "password" : "126735ttydujdsbs"
        }
        self.double_register_data = {
            "email" : "email@gmail.com",
            "username" : "johnny",
            "password" : "126735ttwywibe"
        }
        self.register_user_data = {
            "email" : "email@gmail.com",
            "password" : "barca12345",
            "username" : "johnny"
        }
        self.login_data = {
            "email" : "email@gmail.com",
            "password" : "barca12345"
        }
        self.admin_login = {
            "email" : "Napoleon@gmail.com",
            "password" : "libya256bce"
        }
        self.edit_title = {
            "new_title":"Invasion of Algiers"
        }
        self.borrow2_data = {
            "status" : "borrow"
        }
        response  = self.client.post('/api/v2/users/login',data=json.dumps(self.login_user),content_type='application/json')
        self.token = json.loads(response.data.decode())
        # token = self.token['token']
        # self.token = json.loads(log_in.data.decode())
        # token = self.token['token']