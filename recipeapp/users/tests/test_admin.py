from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class AdminTests(TestCase):

    def setUp(self):
        """
        setup executed before tests are run
        """

        # set up the client 
        self.client = Client()

        #create an admin user
        admin_user = get_user_model().objects.create_superuser(
            email='admin01@admins.com',
            name='admin01',
            password='admin0001'
        )

        # log the admin user into the platform
        self.client.force_login(admin_user)

        # create a normal user
        normal_user = get_user_model().objects.create_user(
            email='user01@users.com',
            name='user01',
            password='user0001'
        )
