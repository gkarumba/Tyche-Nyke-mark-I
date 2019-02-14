import json
#local imports
from app.tests.v1.test_base import BaseTest

class ValidationsTest(BaseTest):
    """
        Class for methods to validate data from user
    """
    def test_check_space(self):
        response = self.client.post('/api/v1/books',data=json.dumps(self.space_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'], 'Title field cannot be empty')

    def test_check_word(self):
        response = self.client.post('api/v1/books',data=json.dumps(self.word_data),content_type='application/json')
        result = json.loads(response.data)
        #import pdb;pdb.set_trace()
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'], 'Author takes only letters')

    def test_check_borrow(self):
        self.client.post('/api/v1/books',data=json.dumps(self.post_data),content_type='application/json')
        response  = self.client.put('/api/v1/books/borrow/1',data=json.dumps(self.borrowing_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'], 'Wrong status format. Use `borrow` or `return`')

    def test_check_return(self):
        self.client.post('/api/v1/books',data=json.dumps(self.post_data),content_type='application/json')
        response  = self.client.put('/api/v1/books/return/1',data=json.dumps(self.returning_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'], 'Wrong status format. Use `return`')
    
    def test_check_email(self):
        response  =self.client.post('api/v1/users/register',data=json.dumps(self.email_data),content_type='application/json')
        #  self.client.put('/api/v1/books/return/1',data=json.dumps(self.returning_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'], 'wrong email format')

    def test_check_password(self):
        response  =self.client.post('api/v1/users/register',data=json.dumps(self.password_data),content_type='application/json')
        #  self.client.put('/api/v1/books/return/1',data=json.dumps(self.returning_data),content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(result['message'], 'Password must be atleast 8 characters')
        

    
        