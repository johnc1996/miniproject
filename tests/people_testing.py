import unittest
from source.app_test import *


class TestPeople(unittest.TestCase):
    def test_add_to_dictionary(self):
        # Arrange
        dictionary = {}
        key = "1"
        value = "john"

        # Act
        new_dictionary = add_to_dictionary(dictionary, key, value)

        # Assert
        self.assertEqual(new_dictionary, {"1": "john"})

    def test_delete_from_dictionary(self):
        # Arrange
        dictionary = {"1": "john"}
        key = "1"

        # Act
        new_dictionary = delete_dictionary_entry(dictionary, key)

        # Assert
        self.assertEqual(new_dictionary, {})

    def test_key_returned_is_correct(self):
        dictionary = {'1': 'john'}
        expected_key = '2'

        key_returned_from_function = get_key_for_new_value_as_string(dictionary)

        self.assertEqual(expected_key, key_returned_from_function)


if __name__ == "__main__":
    unittest.main()
