# import django test case
from django.test import TestCase

from app.calc import add, subtract

class CalcTest(TestCase):

    def test_add_function(self):
        """
        Test for addition
        """
        self.assertEqual(add(10,189), 199)

    def test_subtract_function(self):
        """
        Test for subtraction
        """
        self.assertEqual(subtract(100, 50), 50)