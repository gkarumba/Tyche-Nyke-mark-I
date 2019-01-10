import unittest
import json
#local import
# from app import create_app
from app.tests.test_base import BaseTest
from app.api.books.v1.models import BooksModel

class EndpointsTests(BaseTest):
    """
        Class for testing the books endpoints
    """
   
    # def test_constructor(self):
    #     """
    #         Method for testing the s cosntructor
    #     """
    #     book = BooksModel('Muqqadimah','Mark Anthony','Fiction','Borrowed')

    #     self.assertEqual(book.title,'Muqqadimah',
    #                                 'The title of the book after creation does\
    #                                 not equal the constructor arguement')
    #     self.assertEqual(book.author,'Mark Anthony',
    #                                 'The title of the book after creation does\
    #                                 not equal the constructor arguement')
    #     self.assertEqual(book.category,'Fiction',
    #                                 'The title of the book after creation does\
    #                                 not equal the constructor arguement')
        # self.assertEqual(book.status,'Borrowed',
        #                             'The title of the book after creation does\
        #                             not equal the constructor arguement')
    
    def test_post_books(self):
        """ 
            Method for testing the posting of books
        """
        response  = self.client.post('/api/v1/books',data=json.dumps(self.post_data),content_type='application/json')
        result = json.loads(response.data)
        # import pdb; pdb.set_trace()
        self.assertEqual(response.status_code, 201)
        self.assertIn(result['message'],'Book has been posted successfully')

    def test_get_books(self):
        """
            Method for testing the retrieving of all books
        """
        self.client.post('/api/v1/books',data=json.dumps(self.post_data),content_type='application/json')
        response  = self.client.get('/api/v1/books',data=json.dumps(self.post_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'OK')

    def test_get_one(self):
        """
            Method for testing retrieving one book
        """
        self.client.post('/api/v1/books',data=json.dumps(self.post_data),content_type='application/json')
        response  = self.client.get('/api/v1/books/1',data=json.dumps(self.post_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'OK')

    def test_edit_book(self):
        """
            Method for testing editing a book
        """
        self.client.post('/api/v1/books',data=json.dumps(self.post_data),content_type='application/json')
        response = self.client.put('/api/v1/books/edit/1',data=json.dumps(self.edit_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'book edited successfully')

    def test_borrow(self):
        """
            Method for testing borrowing a book
        """
        self.client.post('/api/v1/books',data=json.dumps(self.post_data),content_type='application/json')
        response  = self.client.put('/api/v1/books/borrow/1',data=json.dumps(self.borrow_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'book borrowed successfully')

    def test_return(self):
        """
            Method for testing returning a book
        """
        self.client.post('/api/v1/books',data=json.dumps(self.post_data),content_type='application/json')
        response = self.client.put('/api/v1/books/return/1',data=json.dumps(self.return_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'Book has been returned')
    
    def test_not_returned(self):
        """
            Method for testing the not returned books by a user
        """
        self.client.post('api/v1/books',data=json.dumps(self.post_data),content_type='application/json')
        response = self.client.get('/api/v1/books',data=json.dumps(self.return_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'Books not returned by user')

    def test_user_history(self):
        """
            Method for testing the user's borrowing history
        """
        self.client.post('api/v1/books',data=json.dumps(self.post_data),content_type='application/json')
        response = self.client.get('/api/v1/books',data=json.dumps(self.return_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],"User's borrowing history")

if __name__ == "__main__":
    unittest.main()