from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):

    def test_user_email(self):
        """
        test user creation with email 
        """
        email = 'testuser3@gmail.com'
        name = 'testUser3'
        password = 'test0003'

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            name=name,
        )

        self.assertEqual(user.email, email)
        #self.assertTrue(user.check_password(password))

    def test_normalized_email(self):
        """
        test emails are normalized
        """

        email = 'testuser5@TEST.COM'
        name = 'testuser5'
        password = 'test0005'

        user = get_user_model().objects.create_user(
            email=email,
            name=name,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_email_validation(self):
        """
        test that an invalid email entry raises a value error
        """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testUser6', 'test0006')