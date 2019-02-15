import unittest
import json
from app.tests.v1.test_base import BaseTest

class EndpointsTests(BaseTest):
    """
        Class for testing the books endpoints
    """
    def test_add_book(self):
        """ 
            Method for testing the user registration
        """
        response  = self.client.post('/api/v2/books',data=json.dumps(self.post_data), headers={'Authorization':'Bearer '+self.token['token'],'content_type':'application/json'})
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertIn(result['message'],'Only Admin is allowed to add a book')

    def test_route_protection(self):
        """ 
            Method for testing the route protection
        """
        response  = self.client.post('/api/v2/books',data=json.dumps(self.post_data), content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 401)
        self.assertIn(result['message'],'Protected Route. Add token to access it')

    def test_get_all_books(self):
        """Method to test the get all books"""
        response  = self.client.get('/api/v2/books',data=json.dumps(self.post_data), headers={'Authorization':'Bearer '+self.token['token'],'content_type':'application/json'})
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'Books in the library')

    def test_get_one_book(self):
        """Method to test the get one book"""
        response  = self.client.get('/api/v2/books/2',data=json.dumps(self.post_data), headers={'Authorization':'Bearer '+self.token['token'],'content_type':'application/json'})
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'Book Found')

    def test_get_one_unavailable_book(self):
        """Method to test the get one book"""
        response  = self.client.get('/api/v2/books/999',data=json.dumps(self.post_data), headers={'Authorization':'Bearer '+self.token['token'],'content_type':'application/json'})
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'],'Invalid ID.No book found')
    
    # def test_edit_book_title(self):
    #     """Method to test a book edit"""
    #     response  = self.client.post('/api/v2/users/login',data=json.dumps(self.admin_login),content_type='application/json')
    #     self.token = json.loads(response.data.decode())
    #     response  = self.client.put('/api/v2/books/title/2',data=json.dumps(self.edit_title), headers={'Authorization':'Bearer '+self.token['token'],'content_type':'application/json'})
    #     result = json.loads(response.data)
    #     import pdb; pdb.set_trace()
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(result['message'],'Book edited successfully')

    # def test_borrow_book(self):
    #     """Method to test the borrow book"""
    #     response  = self.client.post('/api/v2/books/borrow/2',data=json.dumps({'status' : "borrow"}), headers={'Authorization':'Bearer '+self.token['token'],'content_type':'application/json'})
    #     result = json.loads(response.data)
    #     # import pdb; pdb.set_trace()
    #     self.assertEqual(response.status_code, 201)
    #     self.assertIn(result['message'],'Book borrowed successfully')