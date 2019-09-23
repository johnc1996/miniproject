import unittest
from source.round import *


class TestDrinkAdd(unittest.TestCase):
    def test_added_order_in_dictionary(self):
        # Arrange
        person = "john"
        drink = "tea"
        test_round = Round("danny")

        # Act
        test_round.add_to_order(person, drink)

        # Assert
        self.assertEqual(test_round.orders, {"john": "tea"})


if __name__ == "__main__":
    unittest.main()
