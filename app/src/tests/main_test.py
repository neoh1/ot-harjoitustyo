from unittest import TestCase
from unittest.mock import patch
from main import encrypt_pw


class TestMain(TestCase):

    def setUp(self):
        ...

    # test user
    @patch('main.create_connection', return_value=True)
    def test_create_connection(self, input):
        pass

    def test_encrypt_pw_len(self):
        self.assertEqual(len(encrypt_pw('passu')), 160,
                         "Password len is not 160")
