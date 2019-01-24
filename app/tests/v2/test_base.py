import unittest
import json
#local import 
from app import create_app

class BaseTest(unittest.TestCase):
    """
    Class for setting up the base test
    """
    def setUp(self):
        """
        Class for setting up the database
        """
        self.app_test = create_app(config_name='testing_config')
        self.app_context = self.app_test.app_context()
        self.app_context.push()
        self.client = self.app_test.test_client()
        self.app_test.testing  = True

        self.post_data = {
            'title' : 'Battle of worlds',
            'author' : 'Frederick III',
            'category' : 'History'
        }
        self.edit_data = {
            "updated_title":"Rome",
            # "updated_author":"Cassius Aurelius",
            # "updated_category":"fiction"
        }
        self.borrow_data = {
            "updated_status":"borrow"
        }
        self.return_data = {
            "updated_status":"return"
        }
        # self.unreturned_data = {
        #     "status":"Unavailable"
        # }
        self.register_data = {
            "email":"iamscipio@gmail.com",
            "password":"libya256ce",
            "username":"legion"
        }
        self.login_data = {
            "email":"iamscipio@gmail.com",
            "password":"libya256ce",
        }

        register = self.client.post('/api/v2/users/register',data=json.dumps(self.register_data),content_type='application/json')
        login = self.client.post('/api/v2/users/login',data=json.dumps(self.login_data),content_type='application/json')
        response = json.loads(login.data)
        self.token = json.loads(login.data.decode())
        self.token = self.token['token']
        self.Authorization = {"Authorization" : "Bearer "+self.token}
        
if __name__ == '__main__':
    unittest.main()