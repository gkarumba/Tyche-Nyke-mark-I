import unittest

from app.utilities.token import TokenClass
from app.tests.v1.test_base import BaseTest
from app.api.books.v1.models import BooksModel
tk = TokenClass()

class TokensTests(BaseTest):
    """
        Class for testing the tokens
    """

    def test_token_encode(self):
        """Method for testing token generation"""
        user_id = 1
        response = tk.encode_token(user_id)
        result = tk.decode_token(response)
        self.assertNotIsInstance(result,str)
        self.assertEqual(result,user_id)
