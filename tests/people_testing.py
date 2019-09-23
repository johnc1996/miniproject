import unittest
from source.app_test import *


class TestPeople(unittest.TestCase):
    def test_add_to_dictionary_good_input(self):
        # Arrange
        dictionary = {}
        key = "1"
        value = "john"

        # Act
        new_dictionary = add_to_dictionary(dictionary, key, value)

        # Assert
        self.assertEqual(new_dictionary, {"1": "john"})

    def test_delete_from_dictionary_good_input(self):
        # Arrange
        dictionary = {"1": "john"}
        key = "1"

        # Act
        new_dictionary = delete_dictionary_entry(dictionary, key)

        # Assert
        self.assertEqual(new_dictionary, {})


if __name__ == "__main__":
    unittest.main()
