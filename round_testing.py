import unittest
from app_test import *
from round import *


class TestDrinkAdd(unittest.TestCase):
    def test_add_to_order(self):
        # Arrange
        person = "john"
        drink = "tea"
        test_round = Round("danny")

        # Act
        test_round.add_to_order(person, drink)

        # Assert

    def test_load_past_rounds(self):

