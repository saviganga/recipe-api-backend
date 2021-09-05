# import django test case
from django.test import TestCase

from app.calc import add

class CalcTest(TestCase):

    def test_add_function(self):
        """
        Test for addition
        """
        self.assertEqual(add(10,189), 199)