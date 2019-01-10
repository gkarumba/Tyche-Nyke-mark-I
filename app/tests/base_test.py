import unittest
#local import
from app import create_app

class BaseTest(unittest.TestCase):
    """
        Class for setting up the tests
    """ 
    def setUp():
        """
            Method for setting up the tests
        """
        self.app_test = create_app(config_name="testing_config")
        self.client = self.app_test.test_client()
        self.app_test.testing = True
