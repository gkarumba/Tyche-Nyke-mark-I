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
        self.status_data = {
            "updated_status":"borrowed"
        }