import unittest
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
        self.client = self.app_test.test_client()
        self.app_test.testing  = True

        self.post_data = {
            "title":"Catharge",
            "author":"Cannius Longinus",
            "category":"history"
        }
        self.edit_data = {
            "updated_title":"Rome",
            "updated_author":"Cassius Aurelius",
            "updated_category":"fiction"
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