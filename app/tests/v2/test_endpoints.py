import json
#local imports
from app.tests.v2.test_base import BaseTest
from app.database.database import BooksDB as db

class EndpointsTest(BaseTest):
    """
    Class for the methods to test the endpoints
    """
    def test_post(self):
        """
        Method to test posting a book
        """
        response = self.client.post('/api/v2/books',data=json.dumps(self.post_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn(result['message'],'Book added successfully')

    def test_get(self):
        """
        Method to test getting all posted books
        """
        self.client.post('/api/v2/books',data=json.dumps(self.post_data),content_type='application/json')
        response = self.client.get('/api/v2/books',data=json.dumps(self.post_data),content_type='application/type')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'OK')

    def test_get_one(self):
        self.client.post('/api/v2/books',data=json.dumps(self.post_data),content_type='application/json')
        response = self.client.get('/api/v2/books/1',data=json.dumps(self.post_data),content_type='application/type')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'OK')

    def test_edit_book(self):
        self.client.post('/api/v2/books',data=json.dumps(self.post_data),content_type='application/json')
        response = self.client.put('/api/v2/books/edit/1',data=json.dumps(self.edit_data),content_type='application/type')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn(result['message'],'Book edit successful')

    def test_borrow_book(self):
        self.client.post('/api/v2/books',data=json.dumps(self.post_data),content_type='application/json')
        response = self.client.put('/api/v2/books/borrow/1',data=json.dumps(self.borrow_data),content_type='application/type')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'Book borrowed successfully')

    def test_return_book(self):
        self.client.post('/api/v2/books',data=json.dumps(self.post_data),content_type='application/json')
        response = self.client.put('/api/v2/books/return/1',data=json.dumps(self.return_data),content_type='application/type')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'Book returned successfully')

    def test_unreturned_books(self):
        self.client.post('/api/v2/books',data=json.dumps(self.post_data),content_type='application/json')
        self.client.put('/api/v2/books/borrow/1',data=json.dumps(self.borrow_data),content_type='application/type')
        response = self.client.get('/api/v2/books/unreturned',data=json.dumps(self.borrow_data),content_type='application/type')
        result = json.loads(response.dat)
        self.assertEqual(response.status_code, 200)
        self.assertIn(result['message'],'Unreturned Books')

    def tearDown(self):
        """
        Method for destroying the tablea after running the program
        """
        db.drop_tables()

if __name__ == '__main__':
    unittest.main()
    
    