"""Delete Command Test"""

import unittest
from command.delete import _cmd_del

class TestDelete(unittest.TestCase):
    """Testing the Delete Command"""

    def setUp(self):
        self.basicData = {
            '1' : "One",
            '2' : "Two",
            '3' : "Three",
        }

    def test_invalid_keys(self):
        """Invalid Keys are ignored
        
        Even when the Key exists, it is not deleted
        """
        # This Key is not in basicData
        self.assertFalse(
            _cmd_del(self.basicData, '*')
        )
        # The * Key is invalid
        invalidKeyData = {'*' : "Value"}
        self.assertFalse(
            _cmd_del(invalidKeyData, '*')
        )
        self.assertTrue(
            '*' in invalidKeyData
        )
        # The _ Key is invalid
        invalidKeyData = {'_' : "Value"}
        self.assertFalse(
            _cmd_del(invalidKeyData, '_')
        )
        self.assertTrue(
            '_' in invalidKeyData
        )

    def test_space_keys(self):
        """Keys that are only space."""
        self.assertFalse(
            _cmd_del(self.basicData, '')
        )
        self.assertFalse(
            _cmd_del(self.basicData, ' ')
        )
        self.assertFalse(
            _cmd_del(self.basicData, '  ')
        )
        self.assertFalse(
            _cmd_del(self.basicData, '  ')
        )

    def test_key_not_in_data(self):
        """"""
        self.assertFalse(
            _cmd_del(self.basicData, '4')
        )
        self.assertFalse(
            _cmd_del(self.basicData, 'a')
        )

    def test_delete_1(self):
        """"""
        self.assertTrue(
            _cmd_del(self.basicData, '1')
        )
        self.assertTrue(
            _cmd_del(self.basicData, '3')
        )
        self.assertDictEqual(
            {'2': "Two"},
            self.basicData
        )
