import unittest
#local import
from app import create_app

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
            "updated_status":"Borrowed"
        }