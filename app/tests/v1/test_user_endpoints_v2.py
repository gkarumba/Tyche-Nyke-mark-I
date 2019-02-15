import unittest
import json
from app.tests.v1.test_base import BaseTest
from app.api.books.v2.models import BooksModel

class EndpointsTests(BaseTest):
    """
        Class for testing the books endpoints
    """
    def test_register_user_twice(self):
        """ 
            Method for testing the user registration
        """
        response  = self.client.post('/api/v2/users/register',data=json.dumps(self.register_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'],'user already exists')

    def test_login_user(self):
        """ Method for testing the user login"""   
        response  = self.client.post('/api/v2/users/login',data=json.dumps(self.login_user),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'User logged in successfully')

    def test_login_unregistered_email(self):
        """ Method for testing the user login"""   
        response  = self.client.post('/api/v2/users/login',data=json.dumps(self.login_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'],'Invalid Email Address')

    def test_login_unregistered_password(self):
        """ Method for testing the user login"""   
        response  = self.client.post('/api/v2/users/login',data=json.dumps(self.login_wrong_password),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'],'Invalid logging credentials')

    def test_unreturned_books_user(self):
        """Method to test unreturned books by a user"""
        response = self.client.get('/api/v2/users/books/unreturned/1',data=json.dumps(self.post_data), headers={'Authorization':'Bearer '+self.token['token'],'content_type':'application/json'})
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 401)
        self.assertIn(result['message'],'Only Admin is allowed to check for unreturned books')

    def test_unknown_user_borrowing_history(self):
        """Method to test user borrowing history"""
        response = self.client.get('/api/v2/users/books/history/55',data=json.dumps(self.post_data), headers={'Authorization':'Bearer '+self.token['token'],'content_type':'application/json'})
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'],'Invalid User ID')

    def test_user_borrowing_history(self):
        """Method to test user borrowing history"""
        response = self.client.get('/api/v2/users/books/history/6',data=json.dumps(self.post_data), headers={'Authorization':'Bearer '+self.token['token'],'content_type':'application/json'})
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'Books borrowed by user')
    
